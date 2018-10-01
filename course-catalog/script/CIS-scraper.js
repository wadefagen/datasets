var rp = require('request-promise-native');
var decode = require('unescape');
var parseString = require('xml2js').parseString;

var fastXmlParser = require('fast-xml-parser');
var fs = require("fs");

var output = "Year,Term,YearTerm,Subject,Number,Title\n";

function sleep(ms){
  return new Promise(resolve=>{
      setTimeout(resolve,ms)
  });
};


var run = async function(year, term, yearTerm, url) {
  var xml = await rp(url);
  //const result = parseString(xml);
  var result = fastXmlParser.parse(xml, {ignoreAttributes: false});

  var d = result["ns2:term"]["subjects"]["subject"];

  for (var i = 0; i < d.length; i++) {
    var subjTag = d[i];
    var subject = subjTag["@_id"];
    //console.log(subject)
    var href = subjTag["@_href"];
    
    var xml2 = await rp(href);
    var r2 = fastXmlParser.parse(xml2, {ignoreAttributes: false});
    var d2 = r2["ns2:subject"]["courses"]["course"];
    //console.log(d2);

    for (var j = 0; j < d2.length; j++) {
      var courseTag = d2[j];
      var id = courseTag["@_id"];
      var courseName = courseTag["#text"];

      var txt = year + "," + term + "," + yearTerm + "," + subject + "," + id + ",\"" + decode(courseName).replace("\"", "\"\"") + "\"";
      console.log(txt);
      output += txt + "\n";
    }

    //
    await sleep(2500);    
  }

  fs.writeFileSync("uiuc-course-catalog.csv", output);
};


run(2019, "Spring", "2019-sp", "https://courses.illinois.edu/cisapp/explorer/catalog/2019/spring.xml");


