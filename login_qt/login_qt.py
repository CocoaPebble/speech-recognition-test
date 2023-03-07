from time import sleep
from PyQt6 import QtWidgets
import requests
import re


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # init user login state
        self.user_login_state = False

        # Set the window title
        self.setWindowTitle("User Login")
        self.setMinimumSize(640, 480)

        # Create the UI elements
        # title_label = QtWidgets.QLabel("用户登录")
        email_label = QtWidgets.QLabel("邮箱:")
        self.email_input = QtWidgets.QLineEdit()
        password_label = QtWidgets.QLabel("密码:")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        login_button = QtWidgets.QPushButton("登录")
        register_button = QtWidgets.QPushButton("注册")
        
        # Connect the buttons to their functions
        login_button.clicked.connect(self.login)
        register_button.clicked.connect(self.popup_register)

        # Create the layout
        login_layout = QtWidgets.QVBoxLayout()
        # login_layout.addWidget(title_label)
        login_email_layout = QtWidgets.QHBoxLayout()
        login_email_layout.addWidget(email_label)
        login_email_layout.addWidget(self.email_input)
        login_layout.addLayout(login_email_layout)
        login_password_layout = QtWidgets.QHBoxLayout()
        login_password_layout.addWidget(password_label)
        login_password_layout.addWidget(self.password_input)
        login_layout.addLayout(login_password_layout)
        
        # Create a horizontal layout for the buttons
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(register_button)
        button_layout.addWidget(login_button)

        # Add the button layout to the main layout
        login_layout.addLayout(button_layout)

        # Set the main layout for the window
        self.setLayout(login_layout)
        
        
    def error_popup(self, message):
        # Create the popup window
        popup = QtWidgets.QDialog(self)
        popup.setWindowTitle("Error")
        popup.setMinimumSize(160, 120)
        
        # Create the UI elements
        error_label = QtWidgets.QLabel(message)
        error_ok = QtWidgets.QPushButton("OK")
        
        # Connect the buttons to their functions
        error_ok.clicked.connect(popup.close)
        
        # Create the layout
        popup_layout = QtWidgets.QVBoxLayout()
        popup_layout.addWidget(error_label)
        
        # Create a horizontal layout for the buttons
        error_buttons_layout = QtWidgets.QHBoxLayout()
        error_buttons_layout.addWidget(error_ok)
        popup_layout.addLayout(error_buttons_layout)
        
        # Set the main layout for the window
        popup.setLayout(popup_layout)
        popup.exec()
        
        
    def popup_register(self):
        # Create the popup window
        self.popup = QtWidgets.QDialog(self)
        self.popup.setWindowTitle("注册新用户")
        self.popup.setMinimumSize(320, 240)
        
        # Create the UI elements
        reg_name = QtWidgets.QLabel("名字:")
        self.reg_name_input = QtWidgets.QLineEdit()
        reg_email = QtWidgets.QLabel("邮箱:")
        self.reg_email_input = QtWidgets.QLineEdit()
        reg_password = QtWidgets.QLabel("密码:")
        self.reg_password_input = QtWidgets.QLineEdit()
        self.reg_password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        reg_password2 = QtWidgets.QLabel("确认密码:")
        self.reg_password2_input = QtWidgets.QLineEdit()
        self.reg_password2_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        reg_cancel = QtWidgets.QPushButton("取消")
        reg_register = QtWidgets.QPushButton("注册")
        
        # Connect the buttons to their functions
        reg_cancel.clicked.connect(self.popup.close)
        reg_register.clicked.connect(self.register)
        
        # Create the layout
        self.popup_layout = QtWidgets.QVBoxLayout()
        popup_name_layout = QtWidgets.QHBoxLayout()
        popup_email_layout = QtWidgets.QHBoxLayout()
        popup_password_layout = QtWidgets.QHBoxLayout()
        popup_password2_layout = QtWidgets.QHBoxLayout()
        
        # Add the UI elements to the layout
        popup_name_layout.addWidget(reg_name)
        popup_name_layout.addWidget(self.reg_name_input)
        popup_email_layout.addWidget(reg_email)
        popup_email_layout.addWidget(self.reg_email_input)
        popup_password_layout.addWidget(reg_password)
        popup_password_layout.addWidget(self.reg_password_input)
        popup_password2_layout.addWidget(reg_password2)
        popup_password2_layout.addWidget(self.reg_password2_input)
        self.popup_layout.addLayout(popup_name_layout)
        self.popup_layout.addLayout(popup_email_layout)
        self.popup_layout.addLayout(popup_password_layout)
        self.popup_layout.addLayout(popup_password2_layout)
        
        # Create a horizontal layout for the buttons
        reg_buttons_layout = QtWidgets.QHBoxLayout()
        reg_buttons_layout.addWidget(reg_cancel)
        reg_buttons_layout.addWidget(reg_register)
        self.popup_layout.addLayout(reg_buttons_layout)
        
        # Set the main layout for the window
        self.popup.setLayout(self.popup_layout)
        self.popup.exec()
    
    
    def register(self):
        name = self.reg_name_input.text()
        email = self.reg_email_input.text()
        password = self.reg_password_input.text()
        password2 = self.reg_password2_input.text()
        
        # Check if none of the fields are empty
        if not name or not email or not password or not password2:
            print("All fields are required")
            self.error_popup("All fields are required")
            return
        
        # Check if email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email")
            self.error_popup("Invalid email")
            return
        
        # Check if password is valid
        if len(password) < 8:
            print("Password must be at least 8 characters long")
            self.error_popup("Password must be at least 8 characters long")
            return

        # Check if password is valid
        if password != password2:
            print("Password not match")
            self.error_popup("Password not match")
            return
        
        # send register request to server
        response = requests.post('https://heroku-test-4ufit.herokuapp.com/register', json={"email": email, "password": password,"password2": password2,"name": name})
        print(response)
        
        if response.status_code == 200:
            # show hint message success
            print("Register success")
            sleep(2)
            self.popup.close()
        
        
    def login(self):
        # Check if username and password are valid
        email = self.email_input.text()
        password = self.password_input.text()
        
        # Check if email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email")
            self.error_popup("Invalid email")
            return
            
        # Check if password is valid
        if len(password) < 8:
            print("Password must be at least 8 characters long")
            self.error_popup("Password must be at least 8 characters long")
            return
        
        # send login request to server
        response = requests.post('https://heroku-test-4ufit.herokuapp.com/login', json={"email": email, "password": password})
        
        if response.status_code == 400:
            emessage = response.text
            if emessage == "Email not exists":
                print("Email not exists")
                self.error_popup("邮箱不存在")
                return

            if emessage == "Incorrect password":
                print("Invalid password")
                self.error_popup("密码不正确")
                return
            
        if response.status_code == 200:
            # show hint message success
            print("Login success")
            self.user_login_state = True
            sleep(2)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()
