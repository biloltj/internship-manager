# 🧮 Modern Scientific Calculator

> A sleek and modern desktop scientific calculator built with **Python**, **PySide6**, and a custom dark theme.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-Qt-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</p>

---

# 📖 Overview

Modern Scientific Calculator is a desktop application developed with **PySide6 (Qt for Python)**. It combines a clean user interface with powerful scientific calculations, memory functions, keyboard shortcuts, and calculation history.

Designed for students, engineers, programmers, and anyone who needs a fast and elegant calculator.

---

# ✨ Features

## 🔢 Basic Operations

- ➕ Addition
- ➖ Subtraction
- ✖ Multiplication
- ➗ Division
- % Percentage
- Decimal calculations

---

## 📐 Scientific Functions

- sin()
- cos()
- tan()
- log()
- √ Square Root
- Power (^)
- Parentheses support

---

## 🧠 Memory Functions

- MC — Memory Clear
- MR — Memory Recall
- M+ — Memory Add
- M− — Memory Subtract

---

## 📜 Calculation History

- Stores previous calculations
- Displays history in a sidebar
- Updates automatically after each calculation

---

## ⌨ Keyboard Shortcuts

| Key | Action |
|------|--------|
| 0-9 | Numbers |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| Enter | Calculate |
| Backspace | Delete Last Character |
| Esc | Clear |

---

# 🎨 User Interface

The application features a modern dark theme inspired by professional calculator applications.

### Interface Components

- Large display screen
- Live expression preview
- Scientific function buttons
- Memory buttons
- Calculation history panel
- Responsive button layout
- Dark mode design

---

# 🏗 Project Structure

```text
Scientific_Calculator/
│
├── main.py          # Application entry point
├── logic.py         # Calculator engine
├── ui.py            # User interface
├── styles.py        # Dark theme stylesheet
└── README.md
```

---

# ⚙ Technologies Used

- Python 3
- PySide6 (Qt for Python)
- Math Module
- Regular Expressions (re)
- Qt Style Sheets (QSS)

---

# 🧠 Supported Functions

| Function | Example |
|-----------|---------|
| Addition | 5+10 |
| Subtraction | 20-5 |
| Multiplication | 7×8 |
| Division | 100÷5 |
| Power | 5^2 |
| Square Root | √(25) |
| Percentage | 50% |
| Sine | sin(90) |
| Cosine | cos(0) |
| Tangent | tan(45) |
| Logarithm | log(100) |

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/yourusername/Scientific_Calculator.git
```

## Enter the project

```bash
cd Scientific_Calculator
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

```text
Launch Application
        │
        ▼
Initialize Calculator
        │
        ▼
Load Dark Theme
        │
        ▼
Open Main Window
        │
 ┌──────┴───────────┐
 ▼                  ▼
Calculator      History Panel
        │
        ▼
Scientific Calculations
        │
        ▼
Display Result
```

---

# 📂 Modules

## 📌 main.py

- Starts the application
- Creates the Qt application instance
- Opens the main calculator window

---

## 📌 logic.py

Responsible for:

- Expression parsing
- Mathematical evaluation
- Scientific functions
- Memory management
- Calculation history
- Error handling

---

## 📌 ui.py

Contains:

- Main window
- Calculator buttons
- Keyboard shortcuts
- Display
- History sidebar
- User interaction logic

---

## 📌 styles.py

Provides a custom dark theme including:

- Modern buttons
- Operator colors
- Display styling
- Responsive layout
- Hover effects

---

# 🎯 Error Handling

The calculator safely handles:

- Division by zero
- Invalid expressions
- Syntax errors
- Value errors

Friendly messages are displayed instead of crashing.

---

# 🌟 Highlights

- ✅ Modern dark UI
- ✅ Scientific calculations
- ✅ Memory operations
- ✅ Keyboard shortcuts
- ✅ Calculation history
- ✅ Responsive layout
- ✅ Safe expression evaluation
- ✅ Clean code architecture

---

# 📈 Future Improvements

- 📊 Graph plotting
- 🧮 Matrix calculations
- 📐 Unit converter
- 💱 Currency converter
- 🌙 Theme switching
- 📄 Export calculation history
- 📝 Copy/Paste support

---

# 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature/new-feature

# Commit changes
git commit -m "Added new feature"

# Push changes
git push origin feature/new-feature
```

Then open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## **Bilol Arzykulov**

Python Developer | Desktop Application Developer

- 💻 Passionate about Python & Qt Development
- 🎯 Focused on building clean and modern desktop applications
- 🚀 Always learning new technologies

### Connect with me

- GitHub: https://github.com/biloltj
- LinkedIn: https://linkedin.com/in/bilolorzu

---

# ⭐ Support

If you enjoyed this project, please consider giving it a **⭐ Star** on GitHub.

Your support motivates future improvements and helps others discover the project.

---

<p align="center">
Made with ❤️ by <strong>Bilol Arzykulov</strong> using Python & PySide6.
</p>

