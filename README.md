## Catalogue Management System
A full-stack Catalogue Management System built with Flask, MySQL, HTML/CSS, and JavaScript.
It allows users to create, view, update, and delete catalogues, with clean UI and full API support.
Ideal for managing product or service catalogues in small to mid-scale applications.

 ## Features:
-Create a catalogue (Name, Description, Start & End Date)
-View all catalogues with pagination & filtering
-Update existing catalogue info
-Delete catalogue by ID
-Secure login page with test user credentials
-Search & Filter catalogues by ID
-Backend validation and error handling
-RESTful API structure tested via Postman
-Unit tested using PyTest
-Swagger API Documentation
-Application-level logging with rotating log file

## Technologies Used:
Backend: Python, Flask

Frontend: HTML5, CSS3, JavaScript (Fetch API)

Database: MySQL

Testing: PyTest

Documentation: Swagger

Logging: Python Logging (RotatingFileHandler)

Version Control: Git & GitHub

## 📁 Project Structure

📁 catalogue-management-flask
├── app.py
├── requirements.txt
├── README.md
├── schema.sql
│
├── config
│   └── db-connection.ini
│
├── database
│   └── (contains schema.sql)
│
├── dto
│   ├── __init__.py
│   └── catalogue.py
│
├── exception
│   ├── __init__.py
│   └── catalogue_custom_exceptions.py
│
├── logs
│   └── (auto-generated app.log)
│
├── service
│   ├── __init__.py
│   ├── catalogue_service.py
│   └── user_service.py
│
├── static
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates
│   ├── create.html
│   ├── delete.html
│   ├── index.html
│   ├── login.html
│   ├── update.html
│   └── view_all.html
│
├── test
│   └── test_app.py
│
└── util
    ├── __init__.py
    ├── db_connection_util.py
    └── validators.py



## 🛠 Setup Instructions
Clone the Repository:

git clone https://github.com/your-username/catalogue-management-flask.git
cd catalogue-management-flask

 Create a Virtual Environment (optional)
python -m venv venv
venv\Scripts\activate    # for Windows
# or
source venv/bin/activate # for Mac/Linux

Install Dependencies:
pip install -r requirements.txt

Configure the Database:
Create a MySQL database named: cataloguedb

Run the SQL script:
source schema.sql;
Update config/db-connection.ini with your DB credentials:

[mysql]
host = localhost
user = root
password = yourpassword
database = cataloguedb

 ## Login Credentials:
Use the following test login to access the application:

Username: admin
Password: admin123
(Stored in Users table of your MySQL database.)

▶Run the Application
python app.py
Visit: http://127.0.0.1:5000

## ✅ Test the API with PyTest
pytest

 API Documentation (Swagger)
After starting the app, visit:
👉 http://localhost:5000/apidocs (if Swagger integrated with flasgger)

 Notes:
.gitignore excludes: .pyc, __pycache__, .vscode, venv, *.log, etc.

The app uses server-side validation, logging, and structured exception handling.

No third-party frontend frameworks used—pure HTML/CSS/JS.

Author
Meenakshy Raju
























 











