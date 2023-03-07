import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QInputDialog, QCalendarWidget
import datetime
import requests

class MainWindow(QMainWindow):
    def __init__(self, email, exercises):
        super().__init__()
        self.setWindowTitle("动作列表：" + email)
        self.setGeometry(100, 100, 800, 600)
        
        self.today_date = datetime.date.today()
        self.email_label = QLabel("登录邮箱: " + email, self)
        self.email_label.move(10, 15)
        self.email_label.adjustSize()
        self.today_date_label = QLabel("今天日期: "+ str(self.today_date), self)
        self.today_date_label.move(240, 15)
        self.today_date_label.adjustSize()

        self.table = QTableWidget(self)
        self.table.setGeometry(10, 50, 780, 540)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Date", "Exercise"])

        self.exercises = exercises
        self.filter_by_date(str(self.today_date))
        self.update_table()
        
        self.show_all_button = QPushButton("显示全部", self)
        self.show_all_button.move(570, 10)
        self.show_all_button.clicked.connect(self.show_all_exercises)

        self.filter_button = QPushButton("筛选", self)
        self.filter_button.move(680, 10)
        self.filter_button.clicked.connect(self.show_filter_dialog)
        
        self.select_date_button = QPushButton("Select Date", self)
        self.select_date_button.move(420, 10)
        self.select_date_button.clicked.connect(self.show_calendar_dialog)

    def show_calendar_dialog(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.move(420, 10)
        self.calendar.resize(350, 350)
        self.calendar.showToday()
        
        self.calendar.show()
        # calendar.clicked.connect(self.select_date)
        self.calendar.clicked.connect(lambda: self.select_date(self.calendar.selectedDate().toString("yyyy-MM-dd")))

    def select_date(self, date):
        # print(date)
        self.calendar.close()
        self.exercises = exercises
        self.filter_by_date(date)

    def update_table(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        for date, exercise_list in self.exercises:
            for exercise in exercise_list:
                row = self.table.rowCount()
                self.table.insertRow(row)
                self.table.setItem(row, 0, QTableWidgetItem(date))
                self.table.setItem(row, 1, QTableWidgetItem(exercise))

        # Resize the table to fill the window
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setStretchLastSection(True)

    def show_filter_dialog(self):
        filter_type, ok = QInputDialog.getItem(self, "Filter", "Filter by:", ["Date", "Exercise"], 0, False)
        if ok:
            if filter_type == "Date":
                date, ok = QInputDialog.getText(self, "Filter", "Enter date (YYYY-MM-DD):")
                if ok:
                    self.filter_by_date(date)
            elif filter_type == "Exercise":
                exercise, ok = QInputDialog.getText(self, "Filter", "Enter exercise:")
                if ok:
                    self.filter_by_exercise(exercise)

    def filter_by_date(self, date):
        filtered_exercises = [(d, e) for d, e in self.exercises if d == date]
        self.exercises = filtered_exercises
        if not filtered_exercises:
            self.table.setRowCount(1)
            self.table.setItem(0, 0, QTableWidgetItem(str(self.today_date)))
            self.table.setItem(0, 1, QTableWidgetItem("No exercises today!"))
        else:
            self.update_table()

    def filter_by_exercise(self, exercise):
        filtered_exercises = [(d, e) for d, exercise_list in self.exercises for e in exercise_list if e == exercise]
        self.exercises = filtered_exercises
        self.update_table()
        
    def show_all_exercises(self):
        self.exercises = exercises
        self.update_table()

if __name__ == "__main__":
    email = "test11@gmail.com"
    exercises = [("2023-03-03", ["Push-ups", "Sit-ups", "Dead-bug"]), ("2023-03-04", ["Push-ups", "Sit-ups"]), ("2023-03-05", ["Squats", "Lunges"]), ("2023-03-06", ["Sit-ups"])]
    # url = 'https://heroku-test-4ufit.herokuapp.com/'
    # response = requests.get(url + 'get_user_exercise', json={'email': email})
    # exercises = response.json()
    # print(exercises)

    app = QApplication(sys.argv)
    window = MainWindow(email, exercises)
    window.show()
    sys.exit(app.exec())
