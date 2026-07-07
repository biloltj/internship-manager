# styles.py

DARK_THEME = """
QMainWindow {
    background-color: #121212;
}

QLineEdit {
    background-color: #1E1E1E;
    color: #FFFFFF;
    border: none;
    font-size: 32px;
    font-weight: bold;
    padding: 10px;
    selection-background-color: #333333;
}

QLabel {
    color: #888888;
    font-size: 14px;
    padding-right: 10px;
}

QListWidget {
    background-color: #1E1E1E;
    color: #DDDDDD;
    border: none;
    font-size: 14px;
    padding: 5px;
}

QPushButton {
    background-color: #2D2D2D;
    color: #FFFFFF;
    border: none;
    border-radius: 6px;
    font-size: 18px;
    font-weight: 500;
    min-height: 50px;
    min-width: 50px;
}

QPushButton:hover {
    background-color: #3D3D3D;
}

QPushButton:pressed {
    background-color: #4D4D4D;
}

/* Operator Buttons (+, -, *, /) */
QPushButton[btn_type="operator"] {
    background-color: #FF9500;
    color: #FFFFFF;
}
QPushButton[btn_type="operator"]:hover {
    background-color: #FFAE33;
}
QPushButton[btn_type="operator"]:pressed {
    background-color: #CC7600;
}

/* Equals Button */
QPushButton[btn_type="equals"] {
    background-color: #007AFF;
    color: #FFFFFF;
}
QPushButton[btn_type="equals"]:hover {
    background-color: #3395FF;
}
QPushButton[btn_type="equals"]:pressed {
    background-color: #0062CC;
}

/* Action Buttons (C, CE, Memory) */
QPushButton[btn_type="action"] {
    background-color: #4A4A4A;
    color: #FFFFFF;
}
QPushButton[btn_type="action"]:hover {
    background-color: #5A5A5A;
}
"""