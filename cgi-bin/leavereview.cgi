#!"C:\Program Files\Python37\python.exe"
# Please edit the above line depending on the operating system and the installed Python version

import mysql.connector
import cgi
import json
import os
from json import loads


def main():
    form = cgi.FieldStorage()

    courseName = form["course"].value
    course = findCourse(courseName)
    print("Content-type: text/html\r\n\r")
    if course != "Error: Course not found!":
        printReviewForm(course)
    else:
        print("<meta http-equiv=\"refresh\" content=\"0; URL='coursepage.cgi?course=%s'\" />" % (courseName))


def findCourse(courseName):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="reviewmycourses",
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM courses WHERE course = %s",
                     (courseName,), multi=True)

    myresult = mycursor.fetchone()

    if not myresult is None:
        return myresult[0]
    else:
        return "Error: Course not found!"


def printReviewForm(course):
    print("<!DOCTYPE html>")
    print("<html>")

    print("<head>")
    print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\" charset=\"utf-8\">")
    print("<title>Leave review for %s</title>" % (course))
    print("<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\">")

    print("""<style>
                body {
                    padding-top: 5rem;
                    padding-bottom: 5rem;
                }

                h1, h2, h3, h4, h5, h6 {
                    text-align: center;
                }

                .range {
                    display: table;
                    position: relative;
                    height: 25px;
                    margin-top: 20px;
                    background-color: rgb(255, 255, 255);
                    border-radius: 4px;
                    -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
                    box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
                    cursor: pointer;
                }

                .range input[type=\"range\"] {
                    -webkit-appearance: none !important;
                    -moz-appearance: none !important;
                    -ms-appearance: none !important;
                    -o-appearance: none !important;
                    appearance: none !important;

                    display: table-cell;
                    width: 100%;
                    background-color: transparent;
                    height: 25px;
                    cursor: pointer;
                }
                .range input[type=\"range\"]::-webkit-slider-thumb {
                    -webkit-appearance: none !important;
                    -moz-appearance: none !important;
                    -ms-appearance: none !important;
                    -o-appearance: none !important;
                    appearance: none !important;

                    width: 11px;
                    height: 25px;
                    color: rgb(255, 255, 255);
                    text-align: center;
                    white-space: nowrap;
                    vertical-align: baseline;
                    border-radius: 0px;
                    background-color: rgb(40, 167, 69);
                }

                .range input[type=\"range\"]::-moz-slider-thumb {
                    -webkit-appearance: none !important;
                    -moz-appearance: none !important;
                    -ms-appearance: none !important;
                    -o-appearance: none !important;
                    appearance: none !important;
                    
                    width: 11px;
                    height: 25px;
                    color: rgb(255, 255, 255);
                    text-align: center;
                    white-space: nowrap;
                    vertical-align: baseline;
                    border-radius: 0px;
                    background-color: rgb(40, 167, 69);
                    
                }

                .range output {
                    display: table-cell;
                    padding: 3px 5px 2px;
                    min-width: 40px;
                    color: rgb(0, 0, 0);
                    background-color: rgb(255, 255, 255);
                    text-align: center;
                    text-decoration: none;
                    border-radius: 4px;
                    border-bottom-left-radius: 0;
                    border-top-left-radius: 0;
                    width: 1%;
                    white-space: nowrap;
                    vertical-align: middle;

                    -webkit-transition: all 0.5s ease;
                    -moz-transition: all 0.5s ease;
                    -o-transition: all 0.5s ease;
                    -ms-transition: all 0.5s ease;
                    transition: all 0.5s ease;

                    -webkit-user-select: none;
                    -khtml-user-select: none;
                    -moz-user-select: -moz-none;
                    -o-user-select: none;
                    user-select: none;
                }
                .range input[type=\"range\"] {
                    outline: none;
                }
            </style>
            <script src="http://code.jquery.com/jquery-latest.js"></script>
        </head>

        <body>
            <nav class=\"navbar navbar-expand-md navbar-dark bg-dark fixed-top\">
                <a class=\"navbar-brand\" href=\"../index.html\">ReviewMyCourses</a>
                <button class=\"navbar-toggler\" type=\"button\" data-toggle=\"collapse\" data-target=\"#navbar\"
                    aria-controls=\"navbar\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">
                    <span class=\"navbar-toggler-icon\"></span>
                </button>

                <div class=\"collapse navbar-collapse\" id=\"navbar\">
                <ul class=\"navbar-nav mr-auto\">
                    <li class=\"nav-item active\">
                        <a class=\"nav-link\" href=\"../index.html\">Home</a>
                    </li>
                    <li class=\"nav-item\">
                        <a class=\"nav-link\" href=\"../courses.html\">Courses</a>
                    </li>
                    <li class=\"nav-item\">
                        <a class=\"nav-link\" href=\"../about.html\">About</a>
                    </li>
                </ul>
                <form class=\"form-inline my-2 my-lg-0\" action=\"search.cgi\" method=\"GET\">
                    <input class=\"form-control mr-sm-2\" type=\"text\" name=\"query\" placeholder=\"Search courses\" aria-label=\"Search\">
                    <button class=\"btn btn-outline-success my-2 my-sm-0\" type=\"submit\">Search</button>
                </form>
            </div>
            </nav>
            <main role=\"main\" class=\"container\">

                <section name=\"review\">""")
    print("""<h3>Please leave a review for course %s:</h3>""" % (course))
    print("""<br>
                    <form action=\"reviewtodb.cgi\" method=\"POST\">
                    <p>&#9888; <b>NEVER</b> submit sensitive or personal information, such as passwords, student ID numbers, solutions to material (past, current or upcoming) or email addresses in reviews. &#9888;</p>
                    <input type=\"hidden\" name=\"course\" value=%s>""" % (course))
    print("""<div class=\"form-group row\">
                            <label for=\"author\" class=\"col-md-4 col-form-label\">Author (optional)</label>
                            <div class=\"col-md-8\">
                                <input type=\"text\" class=\"form-control\" name=\"author\">
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"majorMinorId\" class=\"col-md-4 col-form-label\">Your major/minor</label>
                            <div class=\"col-md-8\">
                                <input type=\"text\" class=\"form-control\" name=\"majorMinor\" id=\"majorMinorId\" required>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"semesterId\" class=\"col-md-4 col-form-label\">Semester and year this course was taken</label>
                            <div class=\"col-md-4\">
                                <select name=\"semester\" class=\"form-control\" id=\"semesterId\" required>
                                    <option value=\"\">Semester...</option>
                                    <option value=\"Fall\">Fall</option>
                                    <option value=\"Winter\">Winter</option>
                                    <option value=\"Summer\">Summer</option>
                                </select>
                            </div>
                            <div class=\"col-md-4\">
                                <select name=\"year\" class=\"form-control\" id=\"yearId\" required>
                                    <option value=\"\">Year...</option>
                                    <option value=\"2019\">2019</option>
                                    <option value=\"2018\">2018</option>
                                    <option value=\"2017\">2017</option>
                                    <option value=\"2016\">2016</option>
                                    <option value=\"2015\">2015</option>
                                    <option value=\"2014\">2014</option>
                                    <option value=\"2013\">2013</option>
                                    <option value=\"2012\">2012</option>
                                    <option value=\"2011\">2011</option>
                                    <option value=\"2010\">2010</option>
                                    <option value=\"2009\">2009</option>
                                    <option value=\"2008\">2008</option>
                                    <option value=\"2007\">2007</option>
                                    <option value=\"2006\">2006</option>
                                    <option value=\"2005\">2005</option>
                                    <option value=\"2004\">2004</option>
                                    <option value=\"2003\">2003</option>
                                    <option value=\"2002\">2002</option>
                                    <option value=\"2001\">2001</option>
                                    <option value=\"2000\">2000</option>
                                </select></br>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"profNameId\" class=\"col-md-4 col-form-label\">Name(s) of professor(s)</label>
                            <div class=\"col-md-8\">
                                <input type=\"text\" name=\"profName\" class=\"form-control\" id=\"profNameId\" required>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"profGoodnessId\" class=\"col-md-4 col-form-label\">How good is/are the professor(s)?</label>
                            <div class=\"col-md-8\">
                                <div class=\"range\">
                                    <input type=\"range\" name=\"profGoodness\" class=\"form-control\" id=\"profGoodnessId\" value=\"0\"
                                        min=\"1\" max=\"10\" step=\"0.5\" oninput=\"profGoodnessOutId.value=value\" required>
                                    <output name=\"profGoodnessOut\" id=\"profGoodnessOutId\">/10</output>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"taNameId\" class=\"col-md-4 col-form-label\">Name(s) of TA(s) (if applicable)</label>
                            <div class=\"col-md-8\">
                                <input type=\"text\" name=\"taName\" class=\"form-control\" id=\"taNameId\">
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"taGoodnessId\" class=\"col-md-4 col-form-label\">How good is/are the TA(s) you have
                                interacted with? (0: Not applicable)</label>
                            <div class=\"col-md-8\">
                                <div class=\"range\">
                                    <input type=\"range\" name=\"taGoodness\" class=\"form-control\" id=\"taGoodnessId\" value=\"0\" min=\"0\"
                                        max=\"10\" step=\"0.5\" oninput=\"taGoodnessOutId.value=value\">
                                    <output name=\"taGoodnessOut\" id=\"taGoodnessOutId\">/10</output>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"easinessId\" class=\"col-md-4 col-form-label\">How easy is this course?<br>
                                (1: hardest&ndash;10: easiest)</label>
                            <div class=\"col-md-8\">
                                <div class=\"range\">
                                    <input type=\"range\" name=\"easiness\" class=\"form-control\" id=\"easinessId\" value=\"0\" min=\"1\"
                                        max=\"10\" step=\"0.5\" oninput=\"easinessOutId.value=value\" required>
                                    <output name=\"easinessOut\" id=\"easinessOutId\">/10</output>
                                </div>
                            </div>

                        </div>
                        <div class=\"form-group row\">
                            <label for=\"usefulnessId\" class=\"col-md-4 col-form-label\">How useful is this course?</label>
                            <div class=\"col-md-8\">
                                <div class=\"range\">
                                    <input type=\"range\" name=\"usefulness\" class=\"form-control\" id=\"usefulnessId\" value=\"0\" min=\"1\"
                                        max=\"10\" step=\"0.5\" oninput=\"usefulnessOutId.value=value\" required>
                                    <output name=\"usefulnessOut\" id=\"usefulnessOutId\">/10</output>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"coolnessId\" class=\"col-md-4 col-form-label\">How cool is this course?</label>
                            <div class=\"col-md-8\">
                                <div class=\"range\">
                                    <input type=\"range\" name=\"coolness\" class=\"form-control\" id=\"coolnessId\" value=\"0\" min=\"1\"
                                        max=\"10\" step=\"0.5\" oninput=\"coolnessOutId.value=value\" required>
                                    <output name=\"coolnessOut\" id=\"coolnessOutId\">/10</output>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"workloadId\" class=\"col-md-4 col-form-label\">How heavy is the workload?<br>
                                (1: heaviest&ndash;10: lightest)</label>
                            <div class=\"col-md-8\">
                                <div class=\"range\">
                                    <input type=\"range\" name=\"workload\" class=\"form-control\" id=\"workloadId\" value=\"0\" min=\"1\"
                                        max=\"10\" step=\"0.5\" oninput=\"workloadOutId.value=value\" required>
                                    <output name=\"workloadOut\" id=\"workloadOutId\">/10</output>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"lecturesId\" class=\"col-md-4 col-form-label\">How useful are the lectures?<br>
                                (0: Not applicable)</label>
                            <div class=\"col-md-8\">
                                <div class=\"range\">
                                    <input type=\"range\" name=\"lectures\" class=\"form-control\" id=\"lecturesId\" value=\"0\" min=\"0\"
                                        max=\"10\" step=\"0.5\" oninput=\"lecturesOutId.value=value\" required>
                                    <output name=\"lecturesOut\" id=\"lecturesOutId\">/10</output>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"prereqsId\" class=\"col-md-4 col-form-label\">How useful are the pre-requisites?<br>
                                (0: Not applicable)</label>
                            <div class=\"col-md-8\">
                                <div class=\"range\">
                                    <input type=\"range\" name=\"prereqs\" class=\"form-control\" id=\"prereqsId\" value=\"0\" min=\"0\"
                                        max=\"10\" step=\"0.5\" oninput=\"prereqsOutId.value=value\" required>
                                    <output name=\"prereqsOut\" id=\"prereqsOutId\">/10</output>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"assignmentsId\" class=\"col-md-4 col-form-label\">How easy are the assignments (if
                                any)?<br>
                                (0: No assignments, 1: hardest&ndash;10: easiest)</label>
                            <div class=\"col-md-8\">
                                <div class=\"range\">
                                    <input type=\"range\" name=\"assignments\" class=\"form-control\" id=\"assignmentsId\" value=\"0\"
                                        min=\"0\" max=\"10\" step=\"0.5\" oninput=\"assignmentsOutId.value=value\" required>
                                    <output name=\"assignmentsOut\" id=\"assignmentsOutId\">/10</output>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"textbookId\" class=\"col-md-4 col-form-label\">Is textbook required? If so, what is it?</label>
                            <div class=\"col-md-8\">
                                <input type=\"text\" class=\"form-control\" name=\"textbook\" id=\"textbookId\">
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"recorded\" class=\"col-md-4 col-form-label\">Was this course recorded?</label>
                            <div class=\"col-md-8\">
                                <div class=\"form-check form-check-inline\">
                                    <input class=\"form-check-input\" type=\"radio\" name=\"recorded\" value=\"Yes\">
                                    <label class=\"form-check-label\" for=\"recorded\">Yes</label>
                                </div>
                                <div class=\"form-check form-check-inline\">
                                    <input class=\"form-check-input\" type=\"radio\" name=\"recorded\" value=\"No\" checked=\"checked\">
                                    <label class=\"form-check-label\" for=\"recorded\">No</label>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"gradeId\" class=\"col-md-4 col-form-label\">Your grade (optional):</label>
                            <div class=\"col-md-8\">
                                <select class=\"form-control\" name=\"grade\" id=\"gradeId\">
                                    <option value=\"\">Select grade...</option>
                                    <option value=\"A\">A</option>
                                    <option value=\"A-\">A&ndash;</option>
                                    <option value=\"B+\">B+</option>
                                    <option value=\"B\">B</option>
                                    <option value=\"B-\">B&ndash;</option>
                                    <option value=\"C+\">C+</option>
                                    <option value=\"C\">C</option>
                                    <option value=\"D\">D</option>
                                    <option value=\"F\">F</option>
                                </select></br>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"classAverageId\" class=\"col-md-4 col-form-label\">Class average (if applicable):</label>
                            <div class=\"col-md-8\">
                                <select class=\"form-control\" name=\"classAverage\" id=\"classAverageId\">
                                    <option value=\"\">Unknown/Not applicable</option>
                                    <option value=\"A\">A</option>
                                    <option value=\"A-\">A&ndash;</option>
                                    <option value=\"B+\">B+</option>
                                    <option value=\"B\">B</option>
                                    <option value=\"B-\">B&ndash;</option>
                                    <option value=\"C+\">C+</option>
                                    <option value=\"C\">C</option>
                                    <option value=\"D\">D</option>
                                    <option value=\"F\">F</option>
                                </select></br>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"gradeCurvedId\" class=\"col-md-4 col-form-label\">Did the professor curve the grades?</label>
                            <div class=\"col-md-8\">
                                <select class=\"form-control\" name=\"gradeCurved\" id=\"gradeCurvedId\">
                                    <option value=\"Not applicable\">Not applicable</option>
                                    <option value=\"No curve\">No curve</option>
                                    <option value=\"Rounded up to next letter grade\">Rounded up to next letter grade</option>
                                    <option value=\"Curved up by one full letter grade or more\">Curved up by one full letter
                                        grade or
                                        more</option>
                                    <option value=\"Curved down\">Curved down</option>
                                </select>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"recommendId\" class=\"col-md-4 col-form-label\">Do you recommend this course?</label>
                            <div class=\"col-md-8\">
                                <div class=\"form-check form-check-inline\">
                                    <input class=\"form-check-input\" type=\"radio\" name=\"recommend\" id=\"recommendId\" value=\"Yes\">
                                    <label class=\"form-check-label\" for=\"recordedId\">Yes</label>
                                </div>
                                <div class=\"form-check form-check-inline\">
                                    <input class=\"form-check-input\" type=\"radio\" name=\"recommend\" id=\"recommendId\" value=\"No\" checked=\"checked\">
                                    <label class=\"form-check-label\" for=\"recommendId\">No</label>
                                </div>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"prosConsId\" class=\"col-md-4 col-form-label\">Pros and cons about this course</label>
                            <div class=\"col-md-8\">
                                <textarea class=\"form-control\" rows=\"10\" cols=\"50\" name=\"prosCons\" id=\"prosConsId\" required></textarea>
                            </div>
                        </div>

                        <div class=\"form-group row\">
                            <label for=\"commentsId\" class=\"col-md-4 col-form-label\">Other comments (e.g.: Suggestions for
                                future course takers? Follow up courses to take?)</label>
                            <div class=\"col-md-8\">
                                <textarea class=\"form-control\" rows=\"10\" cols=\"50\" name=\"comments\" id=\"commentsId\"></textarea>
                            </div>
                        </div>
                        <p>&#9888; By submitting, you agree that this review does not contain ANY sensitive or personal information, such as passwords, student ID numbers, solutions to material (past, current or upcoming) or email addresses. &#9888;</p>
                        <center><input class=\"btn btn-success btn-lg btn-block\" type=\"submit\" value=\"I agree, submit review\"></center>
                    </form>
                </section>
            </main>

           <script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" crossorigin=\"anonymous\"></script>
            <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js\" crossorigin=\"anonymous\"></script>
        </body>

        </html>""")


main()
