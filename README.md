# Catalogue Management System

A simple web-based Catalogue Management System built using **Flask** (Python), **HTML**, **CSS**, and **JavaScript**. The app provides full **CRUD (Create, Read, Update, Delete)** functionality for managing catalogues through a web interface.

---

## 📂 Project Structure

project/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── config/
│ └── db-connection.ini
├── dto/
│ ├── init.py
│ └── catalogue.py
├── exception/
│ ├── init.py
│ └── catalogue_custom_exceptions.py
├── service/
│ ├── init.py
│ └── catalogue_service.py
├── util/
│ ├── init.py
│ ├── validators.py
│ └── db_connection_util.py
├── static/
│ ├── css/
│ │ └── style.css
│ └── js/
│ └── script.js
└── templates/
├── index.html
├── create.html
├── update.html
├── delete.html
└── view_all.html



---

## Features

- Create a catalogue (with name, description, start and end date)
- View all catalogues
- Update catalogue info
- Delete catalogue by ID
- Simple, intuitive user interface
- Full API support using Flask

---

##  Setup Instructions

### 1. Clone the Repository


git clone https://github.com/meenakshyraju/catalogue-management-flask.git
cd catalogue-management-flask

2. Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Database
Create your MySQL database

Add your credentials to config/db-connection.ini

5. Run the App
bash
Copy
Edit
python app.py
Open your browser and visit http://127.0.0.1:5000/

🛠 Technologies Used
Backend: Python, Flask

Frontend: HTML5, CSS3, JavaScript (Fetch API)

Database: MySQL

Version Control: Git & GitHub

Author
Meenakshy Raju

 Notes
.pyc, __pycache__, .vscode, and virtual environment folders are excluded using .gitignore

No third-party frontend frameworks were used—pure HTML/CSS/JS















 











