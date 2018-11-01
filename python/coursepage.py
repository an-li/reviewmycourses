#!C:\Program Files\Python37\python.exe

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
    file = open("../files/courses.list", "r")
    text = file.read().replace('\n', '')
    data = loads(text)
    file.close()

    for entry in data:
        if courseName == entry['name']:
            title = entry['title']
            faculty = entry['faculty']
            description = entry['description']
            notesList = entry['notes']
            notes = '<br />'.join(notesList)
            instructors = entry['instructors']
            terms = entry['terms']
            link = entry['link']
            return [title, faculty, description, notes, instructors, terms, link, courseName], 1
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
        print("<form action=\"../../cgi-bin/upload.php\" method=\"POST\">")
        print("<input type=\"file\" name=\"fileToUpload\"></br>")
        print("<input type=\"submit\" class=\"btn btn-primary btn-lg btn-block\" value=\"Upload a document\" name=\"upload\">")
        print("</form>")

        print("</br><p>There are currently no documents for this course.</p>")
        print("<p>Jump to <a href=\"#info\" class=\"btn btn-primary\">Course info</a> <a href=\"#reviews\" class=\"btn btn-primary\">Reviews</a></p>")
        print("</section>")
        print("<section id=\"reviews\">")
        print("<h4>Course reviews</h4></br>")
        filename = ("../files/reviews/%s.review" % (courseInfo[7]))
        print("<a class=\"btn btn-primary btn-lg btn-block\" href=\"leavereview.py?course=%s\">Leave a review</a></br>" %
              (courseInfo[7]))
        if os.path.isfile(filename) and os.path.getsize(filename) > 0:
            file = open(filename, "r+")
            print(file.read())
            file.close()
        else:
            print("<p>There are currently no reviews for this course.</p>")
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
