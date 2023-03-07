import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

import playsound
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect, QAudioDevice


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Login")
        self.setMinimumSize(320, 240)

        # Create input fields
        self.username_label = QLabel("Username:", self)
        self.username_label.move(50, 50)
        self.username_input = QLineEdit(self)
        self.username_input.move(150, 50)

        self.password_label = QLabel("Password:", self)
        self.password_label.move(50, 100)
        self.password_input = QLineEdit(self)
        self.password_input.move(150, 100)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Create login button
        self.login_button = QPushButton("Login", self)
        self.login_button.move(150, 150)
        self.login_button.clicked.connect(self.login)

    def login(self):
        # Check if username and password are valid
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "admin" and password == "password":
            # Open main application window if credentials are valid
            self.close()
            main_window = MainWindow()
            main_window.show()
        else:
            # Display error message if credentials are invalid
            error_label = QLabel("Invalid username or password", self)
            error_label.move(50, 200)
            error_label.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Audio Player")
        self.setWindowIcon(QIcon("icon.png"))
        self.setMinimumSize(500, 400)

        # Initialize media players
        self.media_player1 = QMediaPlayer(self)
        self.media_player2 = QMediaPlayer(self)
        self.media_player3 = QMediaPlayer(self)
        

        # Create buttons
        button1 = QPushButton("Play Audio 1", self)
        button1.setGeometry(50, 50, 150, 50)
        button1.clicked.connect(self.play_audio1)

        button2 = QPushButton("Play Audio 2", self)
        button2.setGeometry(50, 150, 150, 50)
        button2.clicked.connect(self.play_audio2)

        button3 = QPushButton("Play Audio 3", self)
        button3.setGeometry(50, 250, 150, 50)
        button3.clicked.connect(self.play_audio3)

    def play_audio1(self):
        playsound.playsound('../audio/start.mp3')

    def play_audio2(self):
        playsound.playsound('../audio/stop.mp3')

    def play_audio3(self):
        playsound.playsound('../audio/init.mp3')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
