# PYQT5 System Library
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Email Generator and Validator Essential Library
from datetime import datetime
import re, random, calendar

'''
Notes:

    Regular Expression (regex) Library - For Matching the format of an email and Validating
    Random Library                     - For making a Random output
    Datetime                           - For Formating and Validating Birth Month/Year
    PyQt5                              - For the UI of application

'''

class EmailApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email Generator & Validator")
        self.setFixedSize(600, 500)

        self.email_list = []
        self.validated = []

        self.stack = QStackedWidget()
        self.init_ui()
        self.setCentralWidget(self.stack)

    def init_ui(self):
        self.menu_screen()
        self.generate_screen()
        self.validate_screen()

    def menu_screen(self):
        menu = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Email Generator & Validator")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        btn_generate = QPushButton("Generate Email")
        btn_validate = QPushButton("Validate Email")

        btn_generate.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        btn_validate.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        for btn in [btn_generate, btn_validate]:
            btn.setFixedHeight(40)
            btn.setStyleSheet("font-size: 16px;")

        layout.addWidget(title)
        layout.addSpacing(30)
        layout.addWidget(btn_generate)
        layout.addWidget(btn_validate)

        menu.setLayout(layout)
        self.stack.addWidget(menu)

    def generate_screen(self):
        screen = QWidget()
        layout = QVBoxLayout()

        info = QLabel("Generate Emails")
        info.setFont(QFont("Arial", 14, QFont.Bold))
        info.setAlignment(Qt.AlignCenter)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Full Name (e.g. John Doe)")
        self.birth_input = QLineEdit()
        self.birth_input.setPlaceholderText("Birth Year or Birthdate (YYYY or YYYY-MM-DD)")

        btn_user_gen = QPushButton("Generate Using Info")
        btn_random_gen = QPushButton("Generate Randomly")
        btn_back = QPushButton("Back to Menu")

        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)

        btn_user_gen.clicked.connect(self.gen_from_info)
        btn_random_gen.clicked.connect(self.gen_random)
        btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        layout.addWidget(info)
        layout.addWidget(self.name_input)
        layout.addWidget(self.birth_input)
        layout.addWidget(btn_user_gen)
        layout.addWidget(btn_random_gen)
        layout.addWidget(self.output_area)
        layout.addWidget(btn_back)

        screen.setLayout(layout)
        self.stack.addWidget(screen)

    def validate_screen(self):
        screen = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Validate Email")
        label.setFont(QFont("Arial", 14, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")

        btn_validate = QPushButton("Validate")
        btn_back = QPushButton("Back to Menu")
        self.result_label = QLabel()

        btn_validate.clicked.connect(self.validate_email)
        btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        layout.addWidget(label)
        layout.addWidget(self.email_input)
        layout.addWidget(btn_validate)
        layout.addWidget(self.result_label)
        layout.addWidget(btn_back)

        screen.setLayout(layout)
        self.stack.addWidget(screen)

    def gen_from_info(self):
        name = self.name_input.text().strip()
        birth = self.birth_input.text().strip()
        self.email_list = []

        if not name or not birth:
            QMessageBox.warning(self, "Missing Info", "Please provide both name and birth info.")
            return

        try:
            lname, gname, *rest = name.upper().split()
            mname = rest[0] if rest else ''
        except:
            QMessageBox.warning(self, "Name Error", "Please enter full name as 'Last First [Middle]'.")
            return

        try:
            if len(birth) == 4 and birth.isdigit():
                year = int(birth)
                month = day = ''
            else:
                birthdate = datetime.strptime(birth, "%Y-%m-%d")
                year = birthdate.year
                month = calendar.month_name[birthdate.month]
                day = birthdate.day
        except:
            QMessageBox.warning(self, "Birth Error", "Invalid birth format. Use YYYY or YYYY-MM-DD.")
            return

        g = gname[0].lower()
        m = mname[0].lower() if mname else ''
        l = lname[0].lower()
        g_full = gname.lower()
        l_full = lname.lower()
        yy = str(year)[-2:]
        dd = f"{day:02}" if day else ''
        rand = lambda: str(random.randint(10, 99))

        patterns = [
            "{g}{m}{l}_{yy}{dd}",
            "{g_full}{l}_{yy}{dd}",
            "{g}{l_full}_{rand}",
            "{l_full}.{yy}",
            "{g_full}_{l_full}{dd}"
        ]

        for _ in range(10):
            p = random.choice(patterns)
            email = p.format(
                g=g, m=m, l=l, g_full=g_full,
                l_full=l_full, yy=yy, dd=dd, rand=rand()
            )
            self.email_list.append(f"{email}@domain.com")

        self.output_area.setText("\n".join(self.email_list))

    def gen_random(self):
        self.email_list = []
        chars = "abcdefghijklmnopqrstuvwxyz"

        patterns = [
            "{chars}{num}", "{num}{chars}", "{chars}_{num}",
            "{chars1}{chars2}{num}", "{chars1}.{chars2}.{num}"
        ]

        for _ in range(10):
            c1 = ''.join(random.choices(chars, k=random.randint(4, 6)))
            c2 = ''.join(random.choices(chars, k=random.randint(3, 5)))
            num = str(random.randint(10, 99))
            p = random.choice(patterns)
            email = p.format(chars=c1, chars1=c1, chars2=c2, num=num)
            self.email_list.append(f"{email}@domain.com")

        self.output_area.setText("\n".join(self.email_list))

    def validate_email(self):
        email = self.email_input.text().strip()

        if "@" not in email:
            self.result_label.setText("❌ Missing '@' symbol.")
            return

        username = email.split("@")[0]
        if re.match(r'^[a-zA-Z0-9._]+$', username):
            if email in self.validated:
                self.result_label.setText("✅ Already Validated.")
            else:
                self.result_label.setText("✅ Email is valid!")
                self.validated.append(email)
        else:
            self.result_label.setText("❌ Invalid characters in username.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
            background-color: #1e1e1e;
            color: #ffffff;
            font-family: Segoe UI;
        }
        QLineEdit, QTextEdit {
            background-color: #2d2d2d;
            border: 1px solid #3c3c3c;
            padding: 6px;
            color: #ffffff;
        }
        QPushButton {
            background-color: #3a3a3a;
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
        }
        QPushButton:hover {
            background-color: #555;
        }
    """)
    window = EmailApp()
    window.show()
    sys.exit(app.exec_())
