ReviewMyCourses\
Information and detailed reviews for all McGill courses\
Web server: XAMPP Apache 7.2.11\
Python version used: 3.7.1 for Windows 64-bit

Made by:
* Abdullahi Elmi
* An Li
* Tu Tran

Server: XAMPP Apache (running on localhost)

Technologies used (Front-end):
* HTML5/CSS
* Bootstrap (For theming)
* JavaScript (Home page, about page and paginator)

Technologies used (Back-end):
* CGI (Search, upload and review form processing)
* Python (Initialize script, course pages, search engine, review form, review parser)
* JSON (format for courses list)
* PHP and Slim (Uploader)
* MySQL (Database for courses, documents and reviews)

How to run the site:
1. Copy and paste all contents of the cgi-bin folder to the cgi-bin folder of xampp
2. Copy and paste the support_files folder to the xampp folder
3. Copy and paste all html, js, php files and images directory in the root directory to the htdocs folder of xampp
4. Open localhost/cgi-bin/initialization/initall.cgi in browser to initialize the database if it does not exist or to clear and reinitialize the existing database. If user wants to use the website with existing data, open localhost/index.html in browser instead.

Notes:
* Please edit the shabang at the top of all .cgi files written in Python depending on the operating system and the installed Python version.
* Please change the value of upload_max_filesize= in php.ini to at least 10M to allow files of up to 10MB to be uploaded
* The value of date.timezone= must reflect the server's current time zone.
* Three initialization scripts can be found under localhost/cgi-bin/initialization/
* initall.py resets the entire database and initializes the courses database with course info from courses.list file.
* initcourses.py initializes the courses database with course info from courses.list file only. To run every time courses.list has been edited or replaced.
* initdocuments.py initializes the database for documents. To run every time the contents of the documents folder have been edited on the server without using the upload form on the course pages.

Known issues:
* Entering non-ASCII characters in search box will cause the page to display nothing.
* Slides on the About page will not display properly on mobile