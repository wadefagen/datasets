var rp = require('request-promise-native');
var decode = require('unescape');

var fastXmlParser = require('fast-xml-parser');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

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



var run = async function(year, term, yearTerm, url, detailed) {
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

        {id: 'crn', title: 'CRN'},
        {id: 'sectionNumber', title: 'Section'},
        {id: 'statusCode', title: 'Status Code'},
        {id: 'partOfTerm', title: 'Part of Term'},
        {id: 'sectionStatusCode', title: 'Section Status'},
        {id: 'enrollmentStatus', title: 'Enrollment Status'},
        {id: 'type', title: 'Type'},
        {id: 'start', title: 'Start Time'},
        {id: 'end', title: 'End Time'},
        {id: 'daysOfTheWeek', title: 'Days of Week'},
        {id: 'roomNumber', title: 'Room'},
        {id: 'buildingName', title: 'Building'},
        {id: 'instructors', title: 'Instructors'},
    ]
  });

  var xml = await rp(url);
  var result = fastXmlParser.parse(xml, {ignoreAttributes: false});

  var d = result["ns2:term"]["subjects"]["subject"];

  for (var i = 0; i < d.length; i++) {
    var subjTag = d[i];
    var subject = subjTag["@_id"];
    var href = subjTag["@_href"];
    
    var xml2 = await rp(href); await sleep(1000);
    var r2 = fastXmlParser.parse(xml2, {ignoreAttributes: false});
    var d2 = r2["ns2:subject"]["courses"]["course"];

    for (var j = 0; j < d2.length; j++) {
      var course = {};
      course.savedMeeting = false;
      course.savedSection = false;
      course.savedCourse = false;
      course.year = year;
      course.term = term;
      course.yearTerm = yearTerm;
      course.subject = subject;

      var courseTag = d2[j];
      course.number = courseTag["@_id"];
      course.name = courseTag["#text"];
      course.href = courseTag["@_href"];

      if (detailed) {
        // Parse Course:
        try {
          var xml3 = await rp(course.href); await sleep(1000);
          var r3 = fastXmlParser.parse(xml3, {ignoreAttributes: false});
          var d3 = r3["ns2:course"];
          course.description = decode(attributeOrNull(d3, "description"));
          course.creditHours = decode(attributeOrNull(d3, "creditHours"));
          course.sectionInfo = decode(attributeOrNull(d3, "courseSectionInformation"));
          course.degreeAttributes = decode(attributeOrNull(d3, "sectionDegreeAttributes"));
          course.scheduleInformation = decode(attributeOrNull(d3, "classScheduleInformation"));

          var sectionTagList = r3["ns2:course"]["sections"]["section"];
          if (!Array.isArray(sectionTagList)) { sectionTagList = [sectionTagList]; }
          for (var k = 0; k < sectionTagList.length; k++) {
            var sectionTag = sectionTagList[k];

            var section = {};
            section.href = sectionTag["@_href"];
            section.crn = sectionTag["@_id"];

            var xml4 = await rp(section.href); await sleep(1000);
            var r4 = fastXmlParser.parse(xml4, {ignoreAttributes: false});
            var d4 = r4["ns2:section"];

            section.sectionNumber = decode(attributeOrNull(d4, "sectionNumber"));
            section.statusCode = decode(attributeOrNull(d4, "statusCode"));
            section.partOfTerm = d4["partOfTerm"];
            section.sectionStatusCode = decode(attributeOrNull(d4, "sectionStatusCode"));
            section.enrollmentStatus = decode(attributeOrNull(d4, "enrollmentStatus"));

            var meetingTags = d4["meetings"]["meeting"];
            if (!Array.isArray(meetingTags)) { meetingTags = [meetingTags]; }
            for (var l = 0; l < meetingTags.length; l++) {
              var meetingTag = meetingTags[l];

              var meeting = {};
              meeting.type = meetingTag["type"]["@_code"];
              meeting.start = decode(attributeOrNull(meetingTag, "start"));
              meeting.end = decode(attributeOrNull(meetingTag, "end"));
              meeting.daysOfTheWeek = decode(attributeOrNull(meetingTag, "daysOfTheWeek"));
              meeting.roomNumber = meetingTag["roomNumber"];
              meeting.buildingName = decode(attributeOrNull(meetingTag, "buildingName"));

              var instructors = [];
              var instructorTags = meetingTag["instructors"]["instructor"];
              if (!Array.isArray(instructorTags)) { instructorTags = [instructorTags]; }
              for (var m = 0; m < instructorTags.length; m++) {
                instructors.push(instructorTags[m]["#text"]);
              }
              meeting.instructors = instructors.join(";");

              // Ideal save, with all the data:
              var full = { ...course, ...section, ...meeting };
              await csvWriter.writeRecords( [full] );
              course.savedMeeting = true;
              console.log("Completed: " + course.subject + " " + course.number + " " + section.sectionNumber + " at " + meeting.start);
            }

            // Save if unsaved:
            if (!course.savedMeeting) {
              var full = { ...course, ...section };
              await csvWriter.writeRecords( [full] );
              course.savedSection = true;
            }
          }

          if (course.savedMeeting == false && course.savedSection == false) {
            await csvWriter.writeRecords( [course] );
            course.savedCourse = true;
          }
          console.log("Completed: " + course.subject + " " + course.number);
        } catch (e) {
          console.log("!! FAILED !!: " + course.subject + " " + course.number);
          console.error(e);
        }
      } else {
        if (course.savedMeeting == false && course.savedSection == false && course.savedCourse == false) {
          await csvWriter.writeRecords( [course] );
        }
      } 
    }
    
    console.log("Completed: " + course.subject);
  }
};


run(2019, "Fall", "2019-fa", "https://courses.illinois.edu/cisapp/explorer/schedule/2019/fall.xml", true);

//run(2019, "Fall", "2019-fa", "https://courses.illinois.edu/cisapp/explorer/catalog/2019/fall.xml", true);
//run(2018, "Fall", "2018-fa", "https://courses.illinois.edu/cisapp/explorer/catalog/2018/fall.xml", false);

//run(2018, "Spring", "2019-sp", "https://courses.illinois.edu/cisapp/explorer/catalog/2018/spring.xml", false);
//run(2018, "Spring", "2018-sp", "https://courses.illinois.edu/cisapp/explorer/catalog/2018/spring.xml", false);
//run(2017, "Fall", "2017-fa", "https://courses.illinois.edu/cisapp/explorer/catalog/2017/fall.xml", false);


