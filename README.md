ReviewMyCourses\
Information and detailed reviews for all McGill courses\
Web server: XAMPP Apache 7.2.11\
Python version used: 3.7.0 for Windows 64-bit

Made by:
* Abdullahi Elmi
* An Li
* Ngoc Tuan Tran

Technologies used:
* HTML5/CSS (2)
* Bootstrap (for theming) (1)
* CGI (1)
* Python (Initialize script, course pages, review form, review parser) (1)
* XAMPP Apache (running on localhost) (2)
* JSON (format for courses list) (1)
* Canvas (Home page) (1)
* PHP (Search? (maybe Python) and uploader) (1)
* MySQL (database for courses, documents and reviews) (2)

How to run the site:
1. Copy and paste all contents of the cgi-bin folder to the cgi-bin folder of xampp
2. Copy and paste the support_files folder to the xampp folder
3. Copy and paste all html files in the root directory to the htdocs folder of xampp
4. Open localhost/cgi-bin/initialization/initall.py in browser to initialize the database if it does not exist or to clear and reinitialize the existing database. If user wants to use the website with existing data, open localhost/index.html in browser instead.

Notes:
* Three initialization scripts can be found under localhost/cgi-bin/initialization/
** initall.py resets the entire database and initializes the courses database with course info from courses.list file.
** initcourses.py initializes the courses database with course info from courses.list file only. To run every time courses.list has been edited or replaced.
** initdocuments.py initializes the database for documents. To run every time the contents of the documents folder have been edited on the server without using the upload form on the course pages.