# ui.py
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QGridLayout, QListWidget, QLabel)
from PySide6.QtCore import Qt
from logic import CalculatorLogic
from styles import DARK_THEME

class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic = CalculatorLogic()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Modern Scientific Calculator")
        self.setMinimumSize(450, 600)
        self.setStyleSheet(DARK_THEME)

        # Main Layout split into Calculator and History Sidebar
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        h_layout = QHBoxLayout(main_widget)

        # Left Column (Calculator Grid Layout)
        calc_widget = QWidget()
        v_layout = QVBoxLayout(calc_widget)
        v_layout.setContentsMargins(10, 10, 10, 10)
        v_layout.setSpacing(8)

        # Live tracking expression preview label
        self.preview_label = QLabel("")
        self.preview_label.setAlignment(Qt.AlignRight)
        v_layout.addWidget(self.preview_label)

        # Primary input field display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        v_layout.addWidget(self.display)

        # Grid system generation for inputs
        grid_layout = QGridLayout()
        grid_layout.setSpacing(6)
        v_layout.addLayout(grid_layout)

        # Right Column (History View Panel)
        history_widget = QWidget()
        history_layout = QVBoxLayout(history_widget)
        history_title = QLabel("Calculation History")
        history_title.setStyleSheet("font-weight: bold; color: #FFFFFF;")
        self.history_list = QListWidget()
        history_layout.addWidget(history_title)
        history_layout.addWidget(self.history_list)
        
        h_layout.addWidget(calc_widget, stretch=3)
        h_layout.addWidget(history_widget, stretch=1)

        # Map programmatic layout and styles dynamically
        buttons = [
            ('MC', 0, 0, 'action'), ('MR', 0, 1, 'action'), ('M+', 0, 2, 'action'), ('M-', 0, 3, 'action'),
            ('sin(', 1, 0, 'sci'), ('cos(', 1, 1, 'sci'), ('tan(', 1, 2, 'sci'), ('log(', 1, 3, 'sci'),
            ('√(', 2, 0, 'sci'), ('^', 2, 1, 'sci'), ('(', 2, 2, 'sci'), (')', 2, 3, 'sci'),
            ('C', 3, 0, 'action'), ('CE', 3, 1, 'action'), ('%', 3, 2, 'operator'), ('÷', 3, 3, 'operator'),
            ('7', 4, 0, 'num'), ('8', 4, 1, 'num'), ('9', 4, 2, 'num'), ('×', 4, 3, 'operator'),
            ('4', 5, 0, 'num'), ('5', 5, 1, 'num'), ('6', 5, 2, 'num'), ('-', 5, 3, 'operator'),
            ('1', 6, 0, 'num'), ('2', 6, 1, 'num'), ('3', 6, 2, 'num'), ('+', 6, 3, 'operator'),
            ('0', 7, 0, 'num'), ('.', 7, 1, 'num'), ('=', 7, 2, 'equals')
        ]

        for text, row, col, b_type in buttons:
            btn = QPushButton(text)
            btn.setProperty("btn_type", b_type)
            
            # Stretch "=" button across two grid columns for UI balance
            if text == '=':
                grid_layout.addWidget(btn, row, col, 1, 2)
            else:
                grid_layout.addWidget(btn, row, col)
                
            btn.clicked.connect(self.on_button_click)

    def on_button_click(self):
        button = self.sender()
        text = button.text()
        self.process_input(text)

    def process_input(self, text: str):
        """Dispatches operational rules based on key strings."""
        if text in ["Error: Division by 0", "Error: Invalid Input"]:
            return

        if text == "C":
            self.logic.clear()
            self.display.clear()
            self.preview_label.clear()
        elif text == "CE":
            self.logic.backspace()
            # Clean display formatting after string slicing
            disp_text = self.logic.expression.replace('*', '×').replace('/', '÷')
            self.display.setText(disp_text)
        elif text == "MC":
            self.logic.memory_clear()
        elif text == "MR":
            self.display.setText(str(self.logic.memory_recall()))
            self.logic.expression = str(self.logic.memory_recall())
        elif text == "M+":
            self.logic.memory_add(self.display.text())
        elif text == "M-":
            self.logic.memory_subtract(self.display.text())
        elif text == "=":
            res = self.logic.evaluate()
            self.display.setText(res)
            self.preview_label.clear()
            self.update_history_ui()
        else:
            self.logic.append_to_expression(text)
            disp_text = self.logic.expression.replace('*', '×').replace('/', '÷')
            self.display.setText(disp_text)
            self.preview_label.setText(disp_text)

    def update_history_ui(self):
        self.history_list.clear()
        for item in reversed(self.logic.history):
            self.history_list.addItem(item)

    def keyPressEvent(self, event):
        """Maps physical computer key strokes directly to UI operations."""
        key = event.key()
        text = event.text()

        if Qt.Key_0 <= key <= Qt.Key_9:
            self.process_input(text)
        elif key == Qt.Key_Plus:
            self.process_input("+")
        elif key == Qt.Key_Minus:
            self.process_input("-")
        elif text == "*":
            self.process_input("×")
        elif text == "/":
            self.process_input("÷")
        elif key in [Qt.Key_Enter, Qt.Key_Return, Qt.Key_Equal]:
            self.process_input("=")
        elif key == Qt.Key_Backspace:
            self.process_input("CE")
        elif key == Qt.Key_Escape:
            self.process_input("C")
        elif text in [".", "(", ")", "%", "^"]:
            self.process_input(text)
        else:
            super().keyPressEvent(event)