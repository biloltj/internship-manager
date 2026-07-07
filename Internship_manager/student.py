# student.py
import csv
from database import DatabaseManager

class StudentService:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def add_student(self, data):
        query = """
            INSERT INTO students (first_name, last_name, university, student_group, 
                                 direction, supervisor, start_date, end_date, grade, status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        with self.db.get_connection() as conn:
            conn.execute(query, (
                data['first_name'], data['last_name'], data['university'], data['group'],
                data['direction'], data['supervisor'], data['start_date'], data['end_date'],
                data['grade'], data['status'], data['notes']
            ))

    def update_student(self, student_id, data):
        query = """
            UPDATE students SET first_name=?, last_name=?, university=?, student_group=?, 
                                direction=?, supervisor=?, start_date=?, end_date=?, grade=?, status=?, notes=?
            WHERE id=?
        """
        with self.db.get_connection() as conn:
            conn.execute(query, (
                data['first_name'], data['last_name'], data['university'], data['group'],
                data['direction'], data['supervisor'], data['start_date'], data['end_date'],
                data['grade'], data['status'], data['notes'], student_id
            ))

    def delete_student(self, student_id):
        with self.db.get_connection() as conn:
            conn.execute("DELETE FROM students WHERE id=?", (student_id,))

    def get_all_students(self, filter_status=None, search_query=None):
        query = "SELECT * FROM students WHERE 1=1"
        params = []

        if filter_status and filter_status != "All":
            query += " AND status = ?"
            params.append(filter_status)

        if search_query:
            query += " AND (first_name LIKE ? OR last_name LIKE ? OR student_group LIKE ? OR university LIKE ?)"
            like_str = f"%{search_query}%"
            params.extend([like_str, like_str, like_str, like_str])

        with self.db.get_connection() as conn:
            return [dict(row) for row in conn.execute(query, params).fetchall()]

    def get_stats(self):
        with self.db.get_connection() as conn:
            total = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
            active = conn.execute("SELECT COUNT(*) FROM students WHERE status='Active'").fetchone()[0]
            completed = conn.execute("SELECT COUNT(*) FROM students WHERE status='Completed'").fetchone()[0]
            return {"total": total, "active": active, "completed": completed}

    def save_attendance(self, student_id, date_str, status):
        query = """
            INSERT INTO attendance (student_id, date, status)
            VALUES (?, ?, ?)
            ON CONFLICT(student_id, date) DO UPDATE SET status=excluded.status
        """
        with self.db.get_connection() as conn:
            conn.execute(query, (student_id, date_str, status))

    def get_attendance(self, student_id, date_str):
        with self.db.get_connection() as conn:
            row = conn.execute("SELECT status FROM attendance WHERE student_id=? AND date=?", 
                               (student_id, date_str)).fetchone()
            return row['status'] if row else "Present"

    def export_to_csv(self, filename):
        students = self.get_all_students()
        if not students:
            return False
        
        keys = students[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(students)
        return True