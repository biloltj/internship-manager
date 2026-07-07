# main.py
import sys
from PySide6.QtWidgets import QApplication
from ui import CalculatorUI

def main():
    # Initialize the Qt application instance
    app = QApplication(sys.argv)
    
    # Instantiate the application main window
    calculator = CalculatorUI()
    calculator.show()
    
    # Gracefully exit when execution context window gets closed
    sys.exit(app.exec())

if __name__ == "__main__":
    main()