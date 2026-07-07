# ui.py
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
    QStackedWidget, QTableWidget, QTableWidgetItem, QFormLayout, QLineEdit, 
    QComboBox, QDateEdit, QTextEdit, QSpinBox, QMessageBox, QFileDialog, QHeaderView
)
from PySide6.QtCore import Qt, QDate
from student import StudentService

class MainWindow(QMainWindow):
    def __init__(self, student_service: StudentService):
        super().__init__()
        self.service = student_service
        self.selected_student_id = None
        
        self.setWindowTitle("Internship Student Management System")
        self.resize(1100, 700)
        
        self.setup_ui()
        self.switch_page(0)  # Load dashboard initially

    def setup_ui(self):
        # Main Layout splitter container
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 1. Sidebar Navigation
        sidebar = QWidget()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(220)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        sidebar_layout.setSpacing(8)

        title = QLabel("InternTrack Pro")
        title.setObjectName("SidebarTitle")
        sidebar_layout.addWidget(title)

        self.nav_buttons = []
        nav_items = [("📊 Dashboard", 0), ("👥 Students List", 1), ("📅 Attendance", 2)]
        for text, index in nav_items:
            btn = QPushButton(text)
            btn.setObjectName("SidebarBtn")
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, idx=index: self.switch_page(idx))
            sidebar_layout.addWidget(btn)
            self.nav_buttons.append(btn)
        
        sidebar_layout.addStretch()
        main_layout.addWidget(sidebar)

        # 2. Main Content Display Pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setObjectName("ContentArea")
        
        self.create_dashboard_page()
        self.create_students_page()
        self.create_attendance_page()
        
        main_layout.addWidget(self.stacked_widget)

    def switch_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)
        
        if index == 0:
            self.refresh_dashboard()
        elif index == 1:
            self.refresh_student_table()
        elif index == 2:
            self.refresh_attendance_table()

    # --- PAGE CREATION METHODS ---
    
    def create_dashboard_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(30, 30, 30, 30)
        
        header = QLabel("Dashboard Overview")
        header.setStyleSheet("font-size: 22px; font-weight: bold; color: white;")
        layout.addWidget(header)
        
        # Stat Cards layout
        card_layout = QHBoxLayout()
        self.total_card = self.create_stat_card("Total Interns", "0")
        self.active_card = self.create_stat_card("Active Internships", "0")
        self.completed_card = self.create_stat_card("Completed Programs", "0")
        
        card_layout.addWidget(self.total_card["frame"])
        card_layout.addWidget(self.active_card["frame"])
        card_layout.addWidget(self.completed_card["frame"])
        layout.addLayout(card_layout)
        layout.addStretch()
        self.stacked_widget.addWidget(page)

    def create_stat_card(self, label, value):
        frame = QWidget()
        frame.setObjectName("StatCard")
        lay = QVBoxLayout(frame)
        val_lbl = QLabel(value)
        val_lbl.setObjectName("StatValue")
        lbl_lbl = QLabel(label)
        lbl_lbl.setObjectName("StatLabel")
        lay.addWidget(val_lbl)
        lay.addWidget(lbl_lbl)
        return {"frame": frame, "value_label": val_lbl}

    def create_students_page(self):
        page = QWidget()
        main_h_layout = QHBoxLayout(page)
        main_h_layout.setContentsMargins(20, 20, 20, 20)

        # Left Column - Records Table view
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        # Search & Filters
        filter_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by Name, Group, Uni...")
        self.search_input.textChanged.connect(self.refresh_student_table)
        
        self.status_filter = QComboBox()
        self.status_filter.addItems(["All", "Active", "Completed"])
        self.status_filter.currentIndexChanged.connect(self.refresh_student_table)
        
        export_btn = QPushButton("📥 Export CSV")
        export_btn.setObjectName("ActionBtn")
        export_btn.clicked.connect(self.export_csv)

        filter_layout.addWidget(self.search_input, 4)
        filter_layout.addWidget(self.status_filter, 2)
        filter_layout.addWidget(export_btn, 1)
        left_layout.addLayout(filter_layout)

        # Table Component
        self.student_table = QTableWidget()
        self.student_table.setColumnCount(6)
        self.student_table.setHorizontalHeaderLabels(["ID", "Name", "University", "Group", "Supervisor", "Status"])
        self.student_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.student_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.student_table.itemSelectionChanged.connect(self.load_selected_student_to_form)
        left_layout.addWidget(self.student_table)
        
        main_h_layout.addWidget(left_widget, 6)

        # Right Column - Dynamic Management Form Box
        form_widget = QWidget()
        form_widget.setFixedWidth(340)
        form_layout = QVBoxLayout(form_widget)
        
        form_title = QLabel("Student Profile Form")
        form_title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom:10px;")
        form_layout.addWidget(form_title)

        # Define the dictionary directly to ensure all keys exist in memory immediately
        self.inputs = {
            "First Name": QLineEdit(),
            "Last Name": QLineEdit(),
            "University": QLineEdit(),
            "Group": QLineEdit(),
            "Direction/Major": QLineEdit(),
            "Supervisor": QLineEdit(),
            "Start Date": QDateEdit(calendarPopup=True, date=QDate.currentDate()),
            "End Date": QDateEdit(calendarPopup=True, date=QDate.currentDate().addMonths(3)),
            "Grade": QSpinBox(),
            "Status": QComboBox(),
            "Notes": QTextEdit()
        }

        # Safe configurations now that elements exist
        self.inputs["Status"].addItems(["Active", "Completed"])
        self.inputs["Grade"].setRange(0, 100)

        # Add the widgets to the visual layout form sequentially
        f_lay = QFormLayout()
        for label_text, widget in self.inputs.items():
            f_lay.addRow(QLabel(label_text), widget)
        form_layout.addLayout(f_lay)

        # CRUD Form Management Actions Layout block
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("💾 Save / Add")
        save_btn.setObjectName("ActionBtn")
        save_btn.clicked.connect(self.save_student)
        
        delete_btn = QPushButton("🗑️ Delete")
        delete_btn.setObjectName("DeleteBtn")
        delete_btn.clicked.connect(self.delete_student)
        
        clear_btn = QPushButton("🧹 Clear")
        clear_btn.clicked.connect(self.clear_form)
        
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(delete_btn)
        form_layout.addLayout(btn_layout)
        form_layout.addWidget(clear_btn)
        form_layout.addStretch()

        main_h_layout.addWidget(form_widget, 4)
        self.stacked_widget.addWidget(page)

    def create_attendance_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)

        top_layout = QHBoxLayout()
        top_layout.addWidget(QLabel("Date Selection:"))
        self.attendance_date = QDateEdit(calendarPopup=True, date=QDate.currentDate())
        self.attendance_date.dateChanged.connect(self.refresh_attendance_table)
        top_layout.addWidget(self.attendance_date)
        top_layout.addStretch()
        layout.addLayout(top_layout)

        self.attendance_table = QTableWidget()
        self.attendance_table.setColumnCount(4)
        self.attendance_table.setHorizontalHeaderLabels(["ID", "Name", "Status", "Action Toggle"])
        self.attendance_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.attendance_table)

        self.stacked_widget.addWidget(page)

    # --- FUNCTIONAL LOGIC & BACKEND LINKING ---

    def refresh_dashboard(self):
        stats = self.service.get_stats()
        self.total_card["value_label"].setText(str(stats["total"]))
        self.active_card["value_label"].setText(str(stats["active"]))
        self.completed_card["value_label"].setText(str(stats["completed"]))

    def refresh_student_table(self):
        self.student_table.setRowCount(0)
        students = self.service.get_all_students(
            self.status_filter.currentText(),
            self.search_input.text()
        )
        for s in students:
            row = self.student_table.rowCount()
            self.student_table.insertRow(row)
            self.student_table.setItem(row, 0, QTableWidgetItem(str(s['id'])))
            self.student_table.setItem(row, 1, QTableWidgetItem(f"{s['first_name']} {s['last_name']}"))
            self.student_table.setItem(row, 2, QTableWidgetItem(s['university']))
            self.student_table.setItem(row, 3, QTableWidgetItem(s['student_group']))
            self.student_table.setItem(row, 4, QTableWidgetItem(s['supervisor']))
            self.student_table.setItem(row, 5, QTableWidgetItem(s['status']))

    def load_selected_student_to_form(self):
        selected = self.student_table.selectedItems()
        if not selected:
            return
        
        student_id = selected[0].text()
        students = self.service.get_all_students()
        student = next((s for s in students if str(s['id']) == student_id), None)
        
        if student:
            self.selected_student_id = student['id']
            self.inputs["First Name"].setText(student['first_name'])
            self.inputs["Last Name"].setText(student['last_name'])
            self.inputs["University"].setText(student['university'])
            self.inputs["Group"].setText(student['student_group'])
            self.inputs["Direction/Major"].setText(student['direction'])
            self.inputs["Supervisor"].setText(student['supervisor'])
            self.inputs["Start Date"].setDate(QDate.fromString(student['start_date'], Qt.ISODate))
            self.inputs["End Date"].setDate(QDate.fromString(student['end_date'], Qt.ISODate))
            self.inputs["Grade"].setValue(student['grade'] or 0)
            self.inputs["Status"].setCurrentText(student['status'])
            self.inputs["Notes"].setPlainText(student['notes'])

    def save_student(self):
        if not self.inputs["First Name"].text() or not self.inputs["Last Name"].text():
            QMessageBox.warning(self, "Validation Error", "First and Last Names are required fields.")
            return

        data = {
            'first_name': self.inputs["First Name"].text(),
            'last_name': self.inputs["Last Name"].text(),
            'university': self.inputs["University"].text(),
            'group': self.inputs["Group"].text(),
            'direction': self.inputs["Direction/Major"].text(),
            'supervisor': self.inputs["Supervisor"].text(),
            'start_date': self.inputs["Start Date"].date().toString(Qt.ISODate),
            'end_date': self.inputs["End Date"].date().toString(Qt.ISODate),
            'grade': self.inputs["Grade"].value(),
            'status': self.inputs["Status"].currentText(),
            'notes': self.inputs["Notes"].toPlainText()
        }

        if self.selected_student_id:
            self.service.update_student(self.selected_student_id, data)
            QMessageBox.information(self, "Success", "Record modified seamlessly.")
        else:
            self.service.add_student(data)
            QMessageBox.information(self, "Success", "New Student Intern onboarded successfully.")
        
        self.clear_form()
        self.refresh_student_table()

    def delete_student(self):
        if not self.selected_student_id:
            return
        
        confirm = QMessageBox.question(self, "Confirm Erasure", "Are you sure you want to completely erase this record?", 
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.service.delete_student(self.selected_student_id)
            QMessageBox.information(self, "Success", "Record removed from ecosystem database.")
            self.clear_form()
            self.refresh_student_table()

    def clear_form(self):
        self.selected_student_id = None
        for widget in self.inputs.values():
            if isinstance(widget, QLineEdit): widget.clear()
            elif isinstance(widget, QTextEdit): widget.clear()
            elif isinstance(widget, QSpinBox): widget.setValue(0)
            elif isinstance(widget, QComboBox): widget.setCurrentIndex(0)
        self.student_table.clearSelection()

    def refresh_attendance_table(self):
        self.attendance_table.setRowCount(0)
        date_str = self.attendance_date.date().toString(Qt.ISODate)
        students = self.service.get_all_students(filter_status="Active")
        
        for s in students:
            row = self.attendance_table.rowCount()
            self.attendance_table.insertRow(row)
            self.attendance_table.setItem(row, 0, QTableWidgetItem(str(s['id'])))
            self.attendance_table.setItem(row, 1, QTableWidgetItem(f"{s['first_name']} {s['last_name']}"))
            
            current_status = self.service.get_attendance(s['id'], date_str)
            self.attendance_table.setItem(row, 2, QTableWidgetItem(current_status))
            
            btn = QPushButton("Mark Present" if current_status == "Absent" else "Mark Absent")
            btn.clicked.connect(lambda checked, s_id=s['id'], btn_obj=btn, r=row: self.toggle_attendance(s_id, date_str, btn_obj, r))
            self.attendance_table.setCellWidget(row, 3, btn)

    def toggle_attendance(self, student_id, date_str, button, row):
        current_status = self.attendance_table.item(row, 2).text()
        new_status = "Absent" if current_status == "Present" else "Present"
        
        self.service.save_attendance(student_id, date_str, new_status)
        self.attendance_table.setItem(row, 2, QTableWidgetItem(new_status))
        button.setText("Mark Present" if new_status == "Absent" else "Mark Absent")

    def export_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save Data Export", "", "CSV Files (*.csv)")
        if path:
            if self.service.export_to_csv(path):
                QMessageBox.information(self, "Export Complete", "Data converted and written to file successfully.")
            else:
                QMessageBox.warning(self, "Export Failed", "Database records returned empty dataset.")