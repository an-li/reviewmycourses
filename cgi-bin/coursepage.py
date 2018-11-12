#!"C:\Program Files\Python37\python.exe"
# Please edit the above line depending on the operating system and the installed Python version

import mysql.connector
import cgi
import json
import os
from os import path
from json import loads


def main():
    form = cgi.FieldStorage()

    courseName = form["course"].value
    courseInfo, courseFound = findCourse(courseName)
    print("Content-type: text/html\r\n\r")
    printCourseInfo(courseInfo, courseFound)


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
        course = myresult[0]
        title = myresult[1]
        faculty = myresult[2]
        description = myresult[3]
        notes = myresult[4]
        instructors = myresult[5]
        terms = myresult[6]
        link = myresult[7]
        return [title, faculty, description, notes, instructors, terms, link, course], 1
    else:
        return["Error: Course not found!"], 0


def printCourseInfo(courseInfo, courseFound):
    print("<!DOCTYPE html>")
    print("<html>")
    print("<head>")
    print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">")
    print("<title>%s</title>" % (courseInfo[0]))
    print("<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\">")
    print("""<style>
            body {
                padding-top: 5rem;
                padding-bottom: 5rem;
            }

            h1, h2, h3, h4, h5, h6 {
                text-align: center;
            }
        </style>
    </head>""")
    print("<body>")
    print("""<nav class=\"navbar navbar-expand-md navbar-dark bg-dark fixed-top\">
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
                        <a class=\"nav-link\" href=\"courses.py\">Courses</a>
                    </li>
                    <li class=\"nav-item\">
                        <a class=\"nav-link\" href=\"../about.html\">About</a>
                    </li>
                </ul>
                <form class=\"form-inline my-2 my-lg-0\" action=\"search.py\" method=\"GET\">
                    <input class=\"form-control mr-sm-2\" type=\"text\" name=\"query\" placeholder=\"Search courses\" aria-label=\"Search\">
                    <button class=\"btn btn-outline-success my-2 my-sm-0\" type=\"submit\">Search</button>
                </form>
            </div>
            </nav>
        <main role=\"main\" class=\"container\">""")
    print("<section id=\"info\">")
    print("<h3>", courseInfo[0], "</h3>")
    if courseFound != 0:
        print("</br>")
        print("<p><b>Faculty: </b>", courseInfo[1], "</p></br>")
        print("<p><b>Description: </b>", courseInfo[2], "</p></br>")
        print("<p><b>Notes: </b>", courseInfo[3], "</p></br>")
        print("<p><b>Instructor(s): </b>", courseInfo[4], "</p></br>")
        print("<p><b>Term(s): </b>", courseInfo[5], "</p></br>")
        print("<p><b>Link to McGill eCalendar: </b><a href=\"%s\">%s</a></p></br>" %
              (courseInfo[6], courseInfo[6]))
        print("<p>Jump to <a href=\"#documents\" class=\"btn btn-primary\">Documents</a> <a href=\"#reviews\" class=\"btn btn-primary\">Reviews</a></p>")
    print("</section>")
    if courseFound != 0:

        print("<section id=\"documents\">")
        print("<h4>Course documents</h4></br>")

        print("<form action=\"upload.php\" method=\"POST\">")
        print("""<div class=\"form-group row\">
                            <label for=\"title\" class=\"col-md-4 col-form-label\">Title: </label>
                            <div class=\"col-md-8\">
                                <input type=\"text\" class=\"form-control\" name=\"title\">
                            </div>
                        </div>""")
        print("""<div class=\"form-group row\">
                            <label for=\"file\" class=\"col-md-4 col-form-label\">File: </label>
                            <div class=\"col-md-8\">
                                <input type=\"file\" accept=\".txt, .rtf, .pdf, .doc, .docx, .ppt, .pptx, .xls, .xlsx, .ods, .odp, .odt\" name=\"file\" /></br>
                                Accepted extensions: .txt, .rtf, .pdf, .doc, .docx, .ppt, .pptx, .xls, .xlsx, .ods, .odp, .odt
                            </div>
                        </div>""")
        print("<input type=\"hidden\" name=\"course\" value=%s>" %
              (courseInfo[7]))
        print("</br><p>&#9888; By submitting, you agree that these documents cannot be used unfairly and do not contain solutions to upcoming material. &#9888;</p>")
        print("<input type=\"submit\" class=\"btn btn-primary btn-lg btn-block\" value=\"I agree, upload document\" name=\"upload\">")
        print("</form></br>")

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="reviewmycourses",
        )
        mycursor = mydb.cursor()

        # Please update this section
        mycursor.execute(
            "SELECT * FROM documents WHERE course = %s ORDER BY documentid DESC", (courseInfo[7],), multi=True)

        myresults = mycursor.fetchall()

        if mycursor.rowcount > 0:
            for result in myresults:
                print("<p><a href=\"%s\">%s</a> Posted on %s</p></br>" %
                      (result[4], result[2], result[1]))
        else:
            print("<p>There are currently no documents for this course.</p>")
        mydb.close()

        print("<p>Jump to <a href=\"#info\" class=\"btn btn-primary\">Course info</a> <a href=\"#reviews\" class=\"btn btn-primary\">Reviews</a></p>")
        print("</section>")
        print("<section id=\"reviews\">")
        print("<h4>Course reviews</h4></br>")
        print("<a class=\"btn btn-primary btn-lg btn-block\" href=\"leavereview.py?course=%s\">Leave a review</a></br>" %
              (courseInfo[7]))

        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="reviewmycourses",
        )
        mycursor2 = mydb2.cursor()

        mycursor2.execute("SELECT * FROM reviews WHERE course = %s ORDER BY reviewid DESC",
                          (courseInfo[7],), multi=True)

        myresults2 = mycursor2.fetchall()

        if mycursor2.rowcount > 0:
            for result in myresults2:
                print("<p>Review posted on %s</p>" % result[1])
                print("<p><b>Review by</b> %s</p>" % (result[3]))
                print("<p><b>Your major/minor</b>: %s</p>" % (result[4]))
                print(
                    "<p><b>Semester and year this course was taken</b>: %s %s</p>" % (result[5], result[6]))
                print("<p><b>Name(s) of professor(s)</b>: %s</p>" %
                      (result[7]))
                if result[7] != "No Professor(s)":
                    print("<p><b>How good is/are the professor(s)?</b> %s</p>" %
                          (result[8]))
                print(
                    "<p><b>Name(s) of TA(s) (if applicable)</b>: %s</p>" % (result[9]))
                if result[9] != "No TA(s)":
                    print(
                        "<p><b>How good is/are the TA(s) you have interacted with?</b> %s</p>" % (result[10]))
                print("<p><b>How easy is this course?</b> %s</p>" %
                      (result[11]))
                print("<p><b>How useful is this course?</b> %s</p>" %
                      (result[12]))
                print("<p><b>How cool is this course?</b> %s</p>" %
                      (result[13]))
                print("<p><b>How heavy is the workload?</b> %s</p>" %
                      (result[14]))
                print("<p><b>How useful are the lectures?</b> %s</p>" %
                      (result[15]))
                print(
                    "<p><b>How useful are the pre-requisites?</b> %s</p>" % (result[16]))
                print(
                    "<p><b>How easy are the assignments (if any)?</b> %s</p>" % (result[17]))
                print("<p><b>Required textbook(s):</b> %s</p>" %
                      (result[18]))
                print("<p><b>Was this course recorded?</b> %s</p>" %
                      (result[19]))
                print("<p><b>Your grade</b>: %s</p>" % (result[20]))
                print("<p><b>Class average</b>: %s</p>" % (result[21]))
                print("<p><b>Did the professor curve the grades?</b> %s</p>" %
                      (result[22]))
                print("<p><b>Do you recommend this course?</b> %s</p>" %
                      (result[23]))
                print("<p><b>Pros and cons about this course</b>: %s</p>" %
                      (result[24]))
                print(
                    "<p><b>Other comments (e.g.: Suggestions for future course takers? Follow up courses to take?)</b>: %s</p>" % (result[25]))
                print("<p></br></p>")
        else:
            print("<p>There are currently no reviews for this course.</p>")
        mydb2.close()
    print("<p>Jump to <a href=\"#info\" class=\"btn btn-primary\">Course info</a> <a href=\"#documents\" class=\"btn btn-primary\">Documents</a></p>")
    print("</section>")
    print("""</main>
        <script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\"
            crossorigin=\"anonymous\"></script>
        <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\"
            crossorigin=\"anonymous\"></script>
    </body>

    </html>""")


main()
