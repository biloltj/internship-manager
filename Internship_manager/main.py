# main.py
import sys
from PySide6.QtWidgets import QApplication
from database import DatabaseManager
from student import StudentService
from ui import MainWindow
from styles import DARK_THEME

def main():
    app = QApplication(sys.argv)
    
    # Inject application-wide custom styling rulesheet
    app.setStyleSheet(DARK_THEME)
    
    # Core Data Layer Instantiations
    db_manager = DatabaseManager()
    student_service = StudentService(db_manager)
    
    # Fire UI Window viewport instances
    window = MainWindow(student_service)
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()