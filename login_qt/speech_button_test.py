import sys
import speech_recognition as sr
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import QThread, pyqtSignal

class SpeechRecognitionThread(QThread):
    recognized_text = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def run(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=15)
            # audio2 = self.recognizer.listen_in_background(source, self.on_recognized)
        
        try:
            text = self.recognizer.recognize_google(audio, language='zh-CN')
            self.recognized_text.emit(text)
        except sr.UnknownValueError:
            self.recognized_text.emit("Speech recognition could not understand audio")
        except sr.RequestError as e:
            self.recognized_text.emit(f"Could not request results from Speech Recognition service; {e}")

class SpeechRecognitionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Speech Recognition')

        self.button = QPushButton('Start', self)
        self.button.move(50, 50)
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.button.setEnabled(False)
        self.thread = SpeechRecognitionThread()
        self.thread.recognized_text.connect(self.on_recognized_text)
        self.thread.finished.connect(self.on_thread_finished)
        self.thread.start()

    def on_recognized_text(self, text):
        print(text)

    def on_thread_finished(self):
        self.button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpeechRecognitionWidget()
    ex.show()
    sys.exit(app.exec())
