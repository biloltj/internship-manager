# styles.py

DARK_THEME = """
QMainWindow {
    background-color: #121212;
}

/* Sidebar Styling */
#Sidebar {
    background-color: #1e1e1e;
    border-right: 1px solid #2d2d2d;
}

QLabel#SidebarTitle {
    color: #ffffff;
    font-size: 16px;
    font-weight: bold;
    padding: 15px 5px;
}

QPushButton#SidebarBtn {
    background-color: transparent;
    color: #b3b3b3;
    border: none;
    border-radius: 5px;
    padding: 10px 15px;
    text-align: left;
    font-size: 14px;
}

QPushButton#SidebarBtn:hover {
    background-color: #2a2a2a;
    color: #ffffff;
}

QPushButton#SidebarBtn:checked {
    background-color: #007acc;
    color: #ffffff;
    font-weight: bold;
}

/* Main Content Area */
#ContentArea {
    background-color: #121212;
}

/* Dashboard Cards */
QFrame#StatCard {
    background-color: #1e1e1e;
    border: 1px solid #2d2d2d;
    border-radius: 8px;
    padding: 15px;
}

QLabel#StatValue {
    color: #007acc;
    font-size: 28px;
    font-weight: bold;
}

QLabel#StatLabel {
    color: #aaaaaa;
    font-size: 14px;
}

/* Forms & Inputs */
QLineEdit, QComboBox, QDateEdit, QTextEdit, QSpinBox {
    background-color: #1e1e1e;
    color: #ffffff;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
    padding: 6px;
}

QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QTextEdit:focus {
    border: 1px solid #007acc;
}

QLabel {
    color: #e0e0e0;
}

/* Tables */
QTableWidget {
    background-color: #1e1e1e;
    color: #ffffff;
    gridline-color: #2d2d2d;
    border: 1px solid #2d2d2d;
    border-radius: 4px;
}

QHeaderView::section {
    background-color: #2d2d2d;
    color: #ffffff;
    padding: 6px;
    border: 1px solid #121212;
    font-weight: bold;
}

QTableWidget::item:selected {
    background-color: #007acc;
    color: white;
}

/* Buttons */
QPushButton#ActionBtn {
    background-color: #007acc;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 8px 15px;
    font-weight: bold;
}

QPushButton#ActionBtn:hover {
    background-color: #0098ff;
}

QPushButton#DeleteBtn {
    background-color: #cc3333;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 8px 15px;
    font-weight: bold;
}

QPushButton#DeleteBtn:hover {
    background-color: #ff4444;
}
"""