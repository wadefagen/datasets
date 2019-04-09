var rp = require('request-promise-native');
var decode = require('unescape');
var parseString = require('xml2js').parseString;

var fastXmlParser = require('fast-xml-parser');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;
var fs = require("fs");

var output = "Year,Term,YearTerm,Subject,Number,Title\n";

function sleep(ms){
  return new Promise(resolve=>{
      setTimeout(resolve,ms)
  });
};

function attributeOrNull(d, a1, a2) {
  if (a1 && d[a1]) {
    if (a2 && d[a1][a2]) { return d[a1][a2]; }
    else if (!a2)        { return d[a1]; }
  }

  return null;
}



var run = async function(year, term, yearTerm, url) {
  const csvWriter = createCsvWriter({
    path: yearTerm + ".csv",
    header: [
        {id: 'year', title: 'Year'},
        {id: 'term', title: 'Term'},
        {id: 'yearTerm', title: 'YearTerm'},
        {id: 'subject', title: 'Subject'},
        {id: 'number', title: 'Number'},
        {id: 'name', title: 'Name'},
        {id: 'description', title: 'Description'},
        {id: 'creditHours', title: 'Credit Hours'},
        {id: 'sectionInfo', title: 'Section Info'},
        {id: 'degreeAttributes', title: 'Degree Attributes'},
        {id: 'scheduleInformation', title: 'Schedule Information'},
    ]
  });

  var xml = await rp(url);
  var result = fastXmlParser.parse(xml, {ignoreAttributes: false});

  var d = result["ns2:term"]["subjects"]["subject"];

  for (var i = 0; i < d.length; i++) {
    var subjTag = d[i];
    var subject = subjTag["@_id"];
    var href = subjTag["@_href"];
    
    var xml2 = await rp(href);
    var r2 = fastXmlParser.parse(xml2, {ignoreAttributes: false});
    var d2 = r2["ns2:subject"]["courses"]["course"];

    for (var j = 0; j < d2.length; j++) {
      var course = {};
      course.year = year;
      course.term = term;
      course.yearTerm = yearTerm;
      course.subject = subject;

      var courseTag = d2[j];
      course.number = courseTag["@_id"];
      course.name = courseTag["#text"];
      course.href = courseTag["@_href"];

      // Parse Course:
      var xml3 = await rp(course.href);
      var r3 = fastXmlParser.parse(xml3, {ignoreAttributes: false});
      var d3 = r3["ns2:course"];
      course.description = decode(attributeOrNull(d3, "description"));
      course.creditHours = decode(attributeOrNull(d3, "creditHours"));
      course.sectionInfo = decode(attributeOrNull(d3, "courseSectionInformation"));
      course.degreeAttributes = decode(attributeOrNull(d3, "sectionDegreeAttributes"));
      course.scheduleInformation = decode(attributeOrNull(d3, "classScheduleInformation"));

      console.log("Completed: " + course.subject + " " + course.number);
      await csvWriter.writeRecords( [course] );
      await sleep(2500);
    }
  }

  //fs.writeFileSync("uiuc-course-catalog.csv", output);
};


run(2019, "Fall", "2019-fa", "https://courses.illinois.edu/cisapp/explorer/catalog/2019/fall.xml");


