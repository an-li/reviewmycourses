#!"C:\Program Files\Python37\python.exe"
# Please edit the above line depending on the operating system and the installed Python version

import cgi
import json
import os
import datetime
from json import loads

import mysql.connector


def main():
    form = cgi.FieldStorage(keep_blank_values=1)

    course = form["course"].value

    if form["author"].value == "" or form["author"].value == None:
        author = "Anonymous"
    else:
        author = form["author"].value
    majorMinor = form["majorMinor"].value
    semester = form["semester"].value
    year = form["year"].value
    if form["profName"].value == "" or form["profName"].value == None:
        profName = "No Professor(s)"
    else:
        profName = form["profName"].value
    profGoodness = form["profGoodness"].value + "/10"
    taName = form["taName"].value
    if taName == "" or taName == None:
        taName = "No TA(s)"
    taGoodness = form["taGoodness"].value
    if taGoodness == "0":
        taGoodness = "Not applicable"
    elif taGoodness == "0.5":
        taGoodness = "1/10"
    else:
        taGoodness = taGoodness + "/10"
    easiness = form["easiness"].value + "/10"
    usefulness = form["usefulness"].value + "/10"
    coolness = form["coolness"].value + "/10"
    workload = form["workload"].value + "/10"
    lectures = form["lectures"].value
    if lectures == "0":
        lectures = "Not applicable"
    elif lectures == "0.5":
        lectures = "1/10"
    else:
        lectures = lectures + "/10"
    prereqs = form["prereqs"].value
    if prereqs == "0":
        prereqs = "Not applicable"
    elif prereqs == "0.5":
        prereqs = "1/10"
    else:
        prereqs = prereqs + "/10"
    assignments = form["assignments"].value
    if assignments == "0":
        assignments = "No assignments"
    elif assignments == "0.5":
        assignments = "1/10"
    else:
        assignments = assignments + "/10"
    textbook = form["textbook"].value
    if textbook == "" or textbook == None:
        textbook = "No required textbook(s)"
    recorded = form["recorded"].value
    grade = form["grade"].value
    if grade == "" or grade == None:
        grade = "Not provided"
    classAverage = form["classAverage"].value
    if classAverage == "" or classAverage == None:
        classAverage = "Not provided"
    gradeCurved = form["gradeCurved"].value
    recommend = form["recommend"].value
    prosCons = form["prosCons"].value
    if prosCons == "" or prosCons == None:
        prosCons = "None"
    comments = form["comments"].value
    if comments == "" or comments == None:
        comments = "None"

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="reviewmycourses",
    )
    mycursor = mydb.cursor()

    dateTime = ("%s" %
                (datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

    mycursor.execute(
        "INSERT INTO reviews (tstamp, course, author, majorMinor, semester, year, profName, profGoodness, taName, taGoodness, easiness, usefulness, coolness, workload, lectures, prereqs, assignments, textbook, recorded, grade, classAverage, gradeCurved, recommend, prosCons, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [dateTime, course, author, majorMinor, semester, year, profName, profGoodness, taName, taGoodness, easiness, usefulness, coolness, workload, lectures, prereqs, assignments, textbook, recorded, grade, classAverage, gradeCurved, recommend, prosCons, comments])

    mydb.commit()

    print("Content-type: text/html\r\n\r")
    print("<html><body><meta http-equiv=\"refresh\" content=\"0; URL='coursepage.py?course=%s'\" /></body></html>" % (course))


main()
