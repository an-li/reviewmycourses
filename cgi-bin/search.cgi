#!"C:\Program Files\Python37\python.exe"

import mysql.connector
import cgi
import json
import os
from os import path
from json import loads


def main():
    form = cgi.FieldStorage()
    query = form["query"].value
    courseList = search(query)
    print("Content-type: text/html\r\n\r")
    printCourseList(courseList, query)


def search(query):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="reviewmycourses",
    )
    mycursor = mydb.cursor()

    queryList = query.lower().split()

    argsString = "%"
    for x in queryList:
        argsString = argsString + x + "%"

    sql = 'SELECT * FROM courses WHERE upper(title) LIKE %s OR upper(course) LIKE %s'
    args = [argsString, argsString]
    mycursor.execute(sql, args, multi=True)

    myresult = mycursor.fetchall()

    courseList = []

    for entry in myresult:
        if len(queryList) == 1:
            if queryList[0] == entry[0].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])
                return courseList
        elif len(queryList) == 2:
            if "".join(queryList) in entry[0].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])
        elif len(queryList) == 3:
            if queryList[0] in entry[1].lower() and queryList[1] in entry[1].lower() and queryList[2] in entry[1].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])
            elif queryList[0] == entry[0].lower() or queryList[1] == entry[0].lower() or queryList[2] == entry[0].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])
        elif len(queryList) > 3:
            if queryList[0] in entry[1].lower() and queryList[1] in entry[1].lower() and queryList[2] in entry[1].lower() and queryList[3] in entry[1].lower() and queryList[len(queryList)-1] in entry[1].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])
            elif queryList[0] == entry[0].lower() or queryList[1] == entry[0].lower() or queryList[2] == entry[0].lower() or queryList[3] == entry[0].lower() or queryList[len(queryList)-1] == entry[0].lower() or queryList[len(queryList)-2] == entry[0].lower() or queryList[len(queryList)-3] == entry[0].lower() or queryList[len(queryList)-4] == entry[0].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])

    if len(queryList) == 1:
        for entry in myresult:
            if queryList[0] in entry[0].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])
        for entry in myresult:
            if queryList[0] not in entry[0].lower() and queryList[0] in entry[1].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])

    if len(queryList) == 2:
        for entry in myresult:
            if queryList[0] in entry[0].lower() and queryList[1] in entry[1].lower() and queryList[1] not in entry[0].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])
            elif queryList[0] == entry[0].lower() or queryList[1] == entry[0].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])

    if len(queryList) == 3:
        for entry in myresult:
            if queryList[0] in entry[0].lower() and queryList[1] in entry[0].lower() and queryList[2] not in entry[1].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])

    if len(queryList) > 3:
        for entry in myresult:
            if queryList[0] in entry[0].lower() and queryList[1] in entry[0].lower() and queryList[2] not in entry[1].lower():
                name = entry[0]
                title = entry[1]
                courseList.append([name, title])

    return courseList


def printCourseList(courseList, query):
    queryList = query.split()
    print("<!DOCTYPE html>")
    print("<html>")
    print("<head>")
    print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">")
    print("<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\">")
    print("<title>Search results for: %s</title>" % query)
    print("""<style>
        body {
            padding-top: 5rem;
            padding-bottom: 5rem;
        }

        h1, h2, h3, h4, h5, h6 {
            text-align: center;
        }
        hr { 
            display: block;
            margin-top: 2em;
            margin-bottom: 2em;
            margin-left: 0%;
            margin-right: 0%;
            border-style: solid;
            border-width: 1px;
            border-color: green;
        } 
        .link {
            font-size: 30px;
            font-weight: bold;
            color: black;
            transition-duration: 0.7s;
        }
        .link:hover {
            color: green;
            text-decoration: none;
        }
        .title {
            font-size: 23px;
            margin-bottom: 10px;
        }
        .easyPaginateNav a {
            padding:5px;
            color: rgb(40, 167, 69);
        }

        .easyPaginateNav a.current {
            font-weight: bold;
            text-decoration: underline;
        }
        </style>
        <script src="http://code.jquery.com/jquery-latest.js"></script>
        <script src="../jquery-easyPaginate.js"></script>
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
        <main role=\"main\" class=\"container\">""")

    print("<h2 class=\"text-center text-black\">")
    print("Search results for: </br> %s" % " ".join(queryList))
    print("</h2>")
    print("<hr>")
    if len(courseList) == 0:
        print("<h1>Nothing Found</h1>")
        print("<div class=\"title text-center\">Sorry, we could not find anything that matched your search query. Please try different keywords.</div>")
    i = 0
    print("<div id=\"courses\">")
    while i < len(courseList):
        print("<dd>")
        print("<a class=\"link\" href=\"coursepage.cgi?course=%s\">" %
              courseList[i][0])
        print("%s:" % courseList[i][0])
        print("</a>")
        print("<div class=\"title\">%s</div>" % courseList[i][1])

        print("<a href=\"coursepage.cgi?course=%s\" class=\"btn btn-outline-success\" role=\"button\" aria-pressed=\"true\">View course</a>" %
              courseList[i][0])
        print("</br>")
        print("</br>")
        print("</br>")
        print("</dd>")
        i += 1
    print("</div>")
    print("""</main>
        <script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" crossorigin=\"anonymous\"></script>
        <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js\"
            crossorigin=\"anonymous\"></script>
        <script>
            $('#courses').easyPaginate({
                paginateElement: 'dd',
                elementsPerPage: 50
            });
        </script>
    </body>
    </html>""")


main()
