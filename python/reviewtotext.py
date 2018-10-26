#!"C:\Program Files\Python37\python.exe"

import cgi
import json
import os
import datetime
from json import loads


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
    if grade == "":
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

    filename = ("../files/reviews/%s.review" % (course))
    file = open(filename, "a+")

    file.write("<p>Review posted on %s at %s</p>" %
               (datetime.datetime.now().strftime("%a, %b %d, %Y"), datetime.datetime.now().strftime("%I:%M %p")))
    file.write("<p><b>Review by</b> %s</p>" % (author))
    file.write("<p><b>Your major/minor</b>: %s</p>" % (majorMinor))
    file.write(
        "<p><b>Semester and year this course was taken</b>: %s %s</p>" % (semester, year))
    file.write("<p><b>Name(s) of professor(s)</b>: %s</p>" % (profName))
    if profName != "No Professor(s)":
        file.write("<p><b>How good is/are the professor(s)?</b> %s</p>" %
                   (profGoodness))
    file.write(
        "<p><b>Name(s) of TA(s) (if applicable)</b>: %s</p>" % (taName))
    if taName != "No TA(s)":
        file.write(
            "<p><b>How good is/are the TA(s) you have interacted with?</b> %s</p>" % (taGoodness))
    file.write("<p><b>How easy is this course?</b> %s</p>" % (easiness))
    file.write("<p><b>How useful is this course?</b> %s</p>" %
               (usefulness))
    file.write("<p><b>How cool is this course?</b> %s</p>" % (coolness))
    file.write("<p><b>How heavy is the workload?</b> %s</p>" % (workload))
    file.write("<p><b>How useful are the lectures?</b> %s</p>" %
               (lectures))
    file.write(
        "<p><b>How useful are the pre-requisites?</b> %s</p>" % (prereqs))
    file.write(
        "<p><b>How easy are the assignments (if any)?</b> %s</p>" % (assignments))
    file.write("<p><b>Required textbook(s):</b> %s</p>" % (textbook))
    file.write("<p><b>Was this course recorded?</b> %s</p>" % (recorded))
    file.write("<p><b>Your grade</b>: %s</p>" % (grade))
    file.write("<p><b>Class average</b>: %s</p>" % (classAverage))
    file.write("<p><b>Did the professor curve the grades?</b> %s</p>" %
               (gradeCurved))
    file.write("<p><b>Do you recommend this course?</b> %s</p>" %
               (recommend))
    file.write("<p><b>Pros and cons about this course</b>: %s</p>" %
               (prosCons))
    file.write(
        "<p><b>Other comments (e.g.: Suggestions for future course takers? Follow up courses to take?)</b>: %s</p>" % (prosCons))
    file.write("<p></br></p>\n\n")
    file.close()

    print("Content-type: text/html\r\n\r")
    print("<html><body>")
    print("<meta http-equiv=\"refresh\" content=\"0; URL='coursepage.py?course=%s'\" /></body></html>" % (course))


main()
