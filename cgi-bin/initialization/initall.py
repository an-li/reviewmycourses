#!"C:\Program Files\Python37\python.exe"
# Please edit the above line depending on the operating system and the installed Python version

# Initialization script for ReviewMyCourses
# Clears and initializes the database for courses, documents and reviews and removes all uploaded documents for all courses

import mysql.connector
import json
import os
import shutil
from os import path
from json import loads


def main():
    if os.path.exists("../../htdocs/documents"):
        # Remove documents folder if exists
        shutil.rmtree("../../htdocs/documents", ignore_errors=True)
    initDatabase()
    initTables()
    initCourses()

    # Go to home page after initializing databases
    print("Content-type: text/html\r\n\r")
    print("<html><body>All databases initialized successfully!</br>Redirecting to home page... Click <a href=\"../../index.html\">here</a> if it does not.")
    print("<meta http-equiv=\"refresh\" content=\"3; URL='../../index.html'\" /></body></html>")


def initDatabase():
    # Initialize and clear database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
    )

    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS reviewmycourses")
    mycursor.execute("CREATE DATABASE reviewmycourses")


def initTables():
    # Initialize tables
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
    mycursor.execute("DROP TABLE IF EXISTS reviews")
    mycursor.execute("""CREATE TABLE reviews (
        reviewid INT AUTO_INCREMENT PRIMARY KEY,
        tstamp TEXT NOT NULL,
        course VARCHAR(255) NOT NULL,
        author TEXT NOT NULL,
        majorMinor TEXT,
        semester TEXT,
        year TEXT,
        profName TEXT,
        profGoodness TEXT NOT NULL,
        taName TEXT,
        taGoodness TEXT NOT NULL,
        easiness TEXT NOT NULL,
        usefulness TEXT NOT NULL,
        coolness TEXT NOT NULL,
        workload TEXT NOT NULL,
        lectures TEXT NOT NULL,
        prereqs TEXT NOT NULL,
        assignments TEXT NOT NULL,
        textbook TEXT NOT NULL,
        recorded TEXT,
        grade TEXT NOT NULL,
        classAverage TEXT NOT NULL,
        gradeCurved TEXT,
        recommend TEXT,
        prosCons TEXT NOT NULL,
        comments TEXT NOT NULL
    )""")
    mycursor.execute("DROP TABLE IF EXISTS documents")
    mycursor.execute("""CREATE TABLE documents (
        documentid INT AUTO_INCREMENT PRIMARY KEY,
        tstamp TEXT NOT NULL,
        title TEXT,
        course VARCHAR(255) NOT NULL,
        url TEXT NOT NULL
    )""")


def initCourses():
    # Add courses from courses.list to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="reviewmycourses",
    )

    mycursor = mydb.cursor()

    coursesList = "../../support_files/courses.list"

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
