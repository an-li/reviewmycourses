#!"C:\Program Files\Python37\python.exe"

# Documents database initialization script for ReviewMyCourses
# Initializes only the database for documents with documents that exist in the documents folder

import mysql.connector
import json
import os
import shutil
import datetime
from os import path
from json import loads


def main():
    message = initDocuments()

    # Go to home page after initializing documents database
    print("Content-type: text/html\r\n\r")
    print("<html><body>%s</br>Redirecting to home page... Click <a href=\"../index.html\">here</a> if it does not." % message)
    print("<meta http-equiv=\"refresh\" content=\"3; URL='../index.html'\" /></body></html>")


def initDocuments():
    # Add courses from courses.list to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="reviewmycourses",
    )

    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS documents")
    mycursor.execute("""CREATE TABLE documents (
        documentid INT AUTO_INCREMENT PRIMARY KEY,
        tstamp TEXT NOT NULL,
        title TEXT,
        course VARCHAR(255) NOT NULL,
        url TEXT NOT NULL
    )""")

    documentsDirectory = "../htdocs/documents/"

    if (os.path.isdir(documentsDirectory) and os.listdir(documentsDirectory)):
        for dir in os.listdir(documentsDirectory):
            currentDir = documentsDirectory + os.path.basename(dir)
            for f in os.listdir(currentDir):
                filePath = currentDir + "/" + os.path.basename(f)
                command = "INSERT INTO documents (tstamp, title, course, url) VALUES (%s, %s, %s, %s)"
                info = (datetime.datetime.fromtimestamp(os.path.getmtime(filePath)).strftime('%Y/%m/%d %H:%M:%S'), os.path.basename(
                    f), os.path.basename(dir), ("../documents/" + os.path.basename(dir) + "/" + os.path.basename(f)))
                mycursor.execute(command, info)
        mydb.commit()
        return "All documents initialized successfully!"
    else:
        return "No documents found!"


main()
