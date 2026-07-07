# 🎓 Internship Manager

> A modern desktop application for managing internship students, attendance, and internship progress using **Python**, **PySide6**, and **SQLite**.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-Qt-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

# 📖 Overview

**Internship Manager** is a desktop application that helps organizations and educational institutions efficiently manage internship programs.

It allows administrators to:

- 👨‍🎓 Manage student records
- 📅 Track attendance
- 📊 Monitor internship progress
- 📤 Export records to CSV
- 🎯 View internship statistics from a clean dashboard

---

# ✨ Features

## 📊 Dashboard

- Total interns
- Active internships
- Completed internships
- Real-time statistics

---

## 👥 Student Management

- ➕ Add students
- ✏️ Update student information
- 🗑 Delete student records
- 🔍 Search students instantly
- 📂 Filter by internship status
- 🎓 Store university information
- 👨‍🏫 Assign supervisors
- 📝 Save notes
- ⭐ Record grades

---

## 📅 Attendance

- Daily attendance tracking
- Present / Absent status
- Automatic attendance updates
- SQLite database storage

---

## 📤 CSV Export

Export all internship data into CSV format for:

- Excel
- Google Sheets
- Reports
- Backup

---

# 🖥 User Interface

The application features a modern **dark-themed** desktop interface built with **PySide6**.

### Pages

- 📊 Dashboard
- 👥 Students
- 📅 Attendance

### UI Features

- Modern sidebar navigation
- Responsive layout
- Beautiful dark theme
- Dashboard statistic cards
- Search bar
- Status filters
- Editable forms
- Data tables

---

# 🏗 Project Structure

```text
Internship_Manager/
│
├── database.py          # SQLite database
├── main.py              # Application entry point
├── student.py           # Student CRUD logic
├── ui.py                # Graphical interface
├── styles.py            # Dark stylesheet
├── internship_system.db # SQLite database
└── README.md
````

---

# 🗄 Database Design

## Students Table

| Field         | Type    |
| ------------- | ------- |
| id            | INTEGER |
| first_name    | TEXT    |
| last_name     | TEXT    |
| university    | TEXT    |
| student_group | TEXT    |
| direction     | TEXT    |
| supervisor    | TEXT    |
| start_date    | TEXT    |
| end_date      | TEXT    |
| grade         | INTEGER |
| status        | TEXT    |
| notes         | TEXT    |

---

## Attendance Table

| Field      | Type    |
| ---------- | ------- |
| id         | INTEGER |
| student_id | INTEGER |
| date       | TEXT    |
| status     | TEXT    |

Relationship:

```
Student
    │
    └──────────────► Attendance
```

Each student may have multiple attendance records.

---

# ⚙ Technologies

* Python 3
* PySide6 (Qt for Python)
* SQLite3
* CSV
* Qt Style Sheets (QSS)

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/yourusername/Internship_Manager.git
```

## Move into the project

```bash
cd Internship_Manager
```

## Install dependencies

```bash
pip install PySide6
```

## Run the application

```bash
python main.py
```

---

# 📸 Application Workflow

```
Launch Application
        │
        ▼
Initialize SQLite Database
        │
        ▼
Load Dark Theme
        │
        ▼
Open Main Window
        │
 ┌──────┴─────────┐
 ▼                ▼
Dashboard      Students
                    │
                    ▼
             Attendance
                    │
                    ▼
               Export CSV
```

---

# 📂 Main Modules

## `database.py`

Responsible for:

* Creating SQLite database
* Initializing tables
* Managing database connections

---

## `student.py`

Handles:

* Create student
* Update student
* Delete student
* Search students
* Attendance management
* CSV export

---

## `ui.py`

Provides:

* Dashboard
* Student management page
* Attendance page
* Forms
* Tables
* Dialogs

---

## `styles.py`

Contains the custom Qt Style Sheet used for the application's dark theme.

---

# 🎨 Screens

* 📊 Dashboard
* 👥 Student Management
* 📅 Attendance Tracking

*(Add screenshots here)*

```
screenshots/
├── dashboard.png
├── students.png
└── attendance.png
```

---

# 📈 Future Improvements

* 🔐 User Login
* 📄 PDF Export
* 📧 Email Notifications
* 📊 Charts & Analytics
* 🌍 Multi-language Support
* ☁ Cloud Database
* 📱 Mobile Version

---

# 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature/new-feature

# Commit changes
git commit -m "Added new feature"

# Push
git push origin feature/new-feature
```

Then open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Your Name**

Python Developer

GitHub: [https://github.com/yourusername](https://github.com/yourusername)

LinkedIn: [https://linkedin.com/in/yourusername](https://linkedin.com/in/yourusername)

---

# ⭐ Support

If you like this project, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and supports future development.

---
<p align="center">
Made with ❤️ by <strong>Bilol Arzykulov</strong> using Python, PySide6 & SQLite.
</p>
