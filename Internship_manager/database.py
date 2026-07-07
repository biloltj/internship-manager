# database.py
import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="internship_system.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row  # Access columns by name
        return conn

    def init_db(self):
        """Creates tables if they do not exist."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Students Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    university TEXT,
                    student_group TEXT,
                    direction TEXT,
                    supervisor TEXT,
                    start_date TEXT,
                    end_date TEXT,
                    grade INTEGER,
                    status TEXT DEFAULT 'Active',
                    notes TEXT
                )
            """)
            
            # Attendance Table (Tracked by date per student)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    date TEXT,
                    status TEXT,
                    FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
                    UNIQUE(student_id, date)
                )
            """)
            conn.commit()