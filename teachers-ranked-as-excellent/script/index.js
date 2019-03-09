/*
 * For PDF Conversion:
 *   pdftotext -layout <input>.pdf <output>.txt
 */
 
var rawTxtPath = "../raw_txt/";
var rawCSVPath = "../csv/"

var fs = require("fs");
var path = require("path");
String.prototype.contains = function(it) { return this.indexOf(it) != -1; };

var files = fs.readdirSync(rawTxtPath);

var containsCourseData = function(s) {
  return s.match(/\d/) || s.indexOf("*") != -1;
  //return /\d/.test(s);
};


var term_re = /(WINTER|SPRING|SUMMER|FALL).(\d\d\d\d)/;
var page_re = /(PAGE (\d+))|(^\d+$)/;

var isPageBoundry = function (s) {
  s = s.toUpperCase();

  var containsSemester = s.match(term_re);
  var containsPage = s.match(page_re);

  if (containsSemester || containsPage) { return true; }
  else { return false; }
};

var findTerm = function (s) {
  s = s.toUpperCase();

  var semester = term_re.exec(s)[1];
  var year = term_re.exec(s)[2];

  if (semester == "WINTER")      { semester = "wi"; }
  else if (semester == "SPRING") { semester = "sp"; }
  else if (semester == "SUMMER") { semester = "su"; }
  else if (semester == "FALL")   { semester = "fa"; }
  return semester + year;
};

var completeCSV = "";
files.forEach(function (file) {
  console.log("Processing \"" + file + "\"...");
  var results = [];
  var lines = fs.readFileSync(path.join(rawTxtPath, file), "utf8").split("\n");

  var readingIntro = true;
  var unitName = undefined;
  var unitPersons = [];
  var term = "?";

  for (var i = 0; i < lines.length; i++) {
    var line = lines[i].trim();
    if (line.length == 0) { continue; }

    if (readingIntro) {
      line_l = line.toLowerCase();

      // Fall 2003 format
      if (line_l.contains("based on data collected")) {
        var termStr = line_l.substring(
          line_l.indexOf("based on data collected") + "based on data collected".length + 1
        ).trim();

        termStr = termStr.substring(0, termStr.indexOf(")"));
        term = findTerm(termStr);
      }

      // Spring 2017+
      if (line == "ACCOUNTANCY") {
        readingIntro = false;
      }
    }

    if (!readingIntro) {
      if (isPageBoundry(line)) { continue; }

      // When a unit name is `undefined`, the next thing we read is the unit name
      if (unitName === undefined || !containsCourseData(line)) {
        unitName = line;
      }

      else {
        // If there's no numbers on a line, the courses are contained on the next line:
        if (!line.match(/\d/)) {
          line += " " + lines[++i].trim();
        }

        // Find the end of the name -- the space after the optional "* "
        var endOfName = line.indexOf(",") + 2;
        var firstDigit = /\d/.exec(line).index;



        // Split the line into [name][courseString] segments
        var name = line.substring(0, firstDigit).trim();
        var courseString = line.substring(firstDigit).trim();

        var personType = "Instructor";
        if (name.substring(name.length - 2) == "TA") {
          personType = "TA";
          name = name.substring(0, name.length - 2).trim();
        }

        // Check if the name contians a * to denote "Outstanding"
        var ranking = "Excellent";
        if (name[0] == "*") {
          name = name.substring(1);
          ranking = "Outstanding";
        }

        //console.log(name);
        nameSplit = name.split(",");
        var fname = "";
        if (nameSplit.length == 2) { fname = nameSplit[1].trim(); }
        var lname = nameSplit[0].trim();
        if (fname.length > 1) { fname = fname.substring(0, 1); }

        // Parse the coures
        /*
        var personType = "Instructor";
        if (courseString.startsWith("TA")) {
          personType = "TA";
          courseString = courseString.substring(2).trim();
        }
        */

        // In fa2000, teachers with more than two courses have a ","
        // at the end of the line and their courses continue to the next line.
        //
        // For example in f00incl.txt :149,150
        //      *KESLER,D                374,331,
        //                               231,110
        while (courseString[courseString.length - 1] == ",") {
          courseString += lines[++i].trim();
        }

        var courses = [];
        courseString.split(",").forEach(function (course) {
          courses.push(course.trim());
        });

        // Create the object
        var obj = {
          fname: fname,
          lname: lname,
          ranking: ranking,
          role: personType,
          courses: courses,
          unit: unitName,
          term: term
        };
        results.push(obj);
      }
    }
  }

  console.log("  Term: " + term);
  console.log("  Records: " + results.length);

  // Write the output...
  var csv = "term,unit,lname,fname,role,ranking,course\n";
  if (completeCSV == "") { completeCSV = csv; }
  results.forEach(function (obj) {
    obj.courses.forEach(function (course) {
      if (course == "0") { course = "?"; }
      else if (course == "000") { course = "?"; }
      else if (course == "999") { course = "?"; }

      var str = obj.term + "," +
                "\"" + obj.unit + "\"," +
                obj.lname + "," +
                obj.fname + "," +
                obj.role + "," +
                obj.ranking + "," +
                course + "\n";

      csv += str;
      completeCSV += str;
    })
  });

  fs.writeFileSync(path.join(rawCSVPath, "tre-" + term + ".csv"), csv);
});

fs.writeFileSync(path.join(rawCSVPath, "..", "uiuc-tre-dataset.csv"), completeCSV);
