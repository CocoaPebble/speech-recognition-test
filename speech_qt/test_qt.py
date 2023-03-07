import sys
import playsound
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect, QAudioDevice
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton



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
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
