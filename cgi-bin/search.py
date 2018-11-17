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
    # printCourseInfo(courseInfo)
    print(courseList)


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
                course = entry[0]
                title = entry[1]
                courseList.append([course, title])
                return courseList
        elif len(queryList) == 2:
            if "".join(queryList) in entry[0].lower():
                course = entry[0]
                title = entry[1]
                courseList.append([course, title])
        elif len(queryList) == 3:
            if queryList[0] in entry[0].lower() and queryList[1] in entry[1].lower():
                course = entry[0]
                title = entry[1]
                courseList.append([course, title])
            elif queryList[0] in entry[0].lower() or queryList[1] in entry[0].lower():
                course = entry[0]
                title = entry[1]
                courseList.append([course, title])

    if len(queryList) == 1:
        for entry in myresult:
            if queryList[0] in entry[0].lower():
                course = entry[0]
                title = entry[1]
                courseList.append([course, title])
        for entry in myresult:
            if queryList[0] not in entry[0].lower() and queryList[0] in entry[1].lower():
                course = entry[0]
                title = entry[1]
                courseList.append([course, title])

    if len(queryList) == 2:
        for entry in myresult:
            if queryList[0] in entry[0].lower() and queryList[1] in entry[1].lower() and queryList[1] not in entry[0].lower():
                course = entry[0]
                title = entry[1]
                courseList.append([course, title])
            elif queryList[0] in entry[0].lower() or queryList[1] in entry[0].lower():
                course = entry[0]
                title = entry[1]
                courseList.append([course, title])

    return courseList

# def printCourseInfo(courseInfo):


main()
