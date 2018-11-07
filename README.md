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
3. Copy and paste all html files and initall.py in the root directory to the htdocs folder of xampp
4. Open localhost/initall.py in browser to initialize the database if it does not exist or to clear and reinitialize the existing database. If user wants to use the website with existing data, open localhost/index.html in browser instead.