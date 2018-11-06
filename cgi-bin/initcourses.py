#!"C:\Program Files\Python37\python.exe"

# Courses database initialization script for ReviewMyCourses
# Initializes only the database for courses with course list file generated by crawler

import mysql.connector
import json
import os
import shutil
from os import path
from json import loads


def main():
    initCourses()

    # Go to home page after initializing courses database
    print("Content-type: text/html\r\n\r")
    print("<html><body><meta http-equiv=\"refresh\" content=\"0; URL='../index.html'\" /></body></html>")


def initCourses():
    # Add courses from courses.list to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="reviewmycourses",
    )

    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS courses")
    mycursor.execute("""CREATE TABLE courses
    (
        course VARCHAR(255) NOT NULL PRIMARY KEY,
        title TEXT,
        faculty TEXT,
        description TEXT,
        notes TEXT,
        instructors TEXT,
        terms TEXT,
        link TEXT NOT NULL
    )""")

    coursesList = "../../files/courses.list"

    file = open(coursesList, "r")
    text = file.read().replace('\n', '')
    data = loads(text)
    file.close()

    for entry in data:
        course = entry['name']
        if course == None:
            course = ""
        title = entry['title']
        if title == None:
            title = ""
        faculty = entry['faculty']
        if faculty == None:
            faculty = ""
        description = entry['description']
        if description == None:
            description = ""
        notesList = entry['notes']
        notes = '<br />'.join(notesList)
        if notes == None:
            notes = ""
        instructors = entry['instructors']
        if instructors == None:
            instructors = ""
        terms = entry['terms']
        if terms == None:
            terms = ""
        link = entry['link']
        if link == None:
            link = ""

        command = "INSERT INTO courses (course, title, faculty, description, notes, instructors, terms, link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        info = (course, title, faculty, description,
                notes, instructors, terms, link)
        mycursor.execute(command, info)
        mydb.commit()


main()
