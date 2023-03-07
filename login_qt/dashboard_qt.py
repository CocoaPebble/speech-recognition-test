import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QLabel, QVBoxLayout, QHBoxLayout, QWidget

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle('Exercise Dashboard')
        self.setGeometry(100, 100, 800, 600)

        # Create a vertical layout for the main widget
        layout = QVBoxLayout()

        # Create a horizontal layout for the user info
        user_layout = QHBoxLayout()

        # Add the user info to the user layout
        # user_layout.resize(200, 100)
        user_layout.addWidget(QLabel('Username: JohnDoe'))
        user_layout.addWidget(QLabel('Exercises Completed: 10'))

        # Add the user layout to the main layout
        layout.addLayout(user_layout)

        # Create a table widget for the exercise schedule
        table = QTableWidget()

        # Set the table properties
        table.setRowCount(5)
        table.setColumnCount(8)
        table.setHorizontalHeaderLabels(['Exercise', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)
        # table.setEditTriggers(QTableWidget.NoEditTriggers)
        # table.setSelectionBehavior(QTableWidget.SelectRows)

        # Populate the table with sample data
        data = [['Push-ups', '', '', 'X', '', 'X', '', ''],
                ['Sit-ups', '', '', 'X', '', 'X', '', ''],
                ['Plank', '', '', '', '', '', '', 'X'],
                ['Squats', '', '', '', '', 'X', '', 'X'],
                ['Jumping jacks', '', '', 'X', '', '', '', 'X']]
        for row, item in enumerate(data):
            for col, text in enumerate(item):
                table.setItem(row, col, QTableWidgetItem(text))

        # Add the table widget to the main layout
        layout.addWidget(table)

        # Create a widget to hold the main layout
        widget = QWidget()
        widget.setLayout(layout)

        # Set the main widget of the window
        self.setCentralWidget(widget)

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the dashboard window
    window = Dashboard()

    # Show the window
    window.show()

    # Run the event loop
    sys.exit(app.exec())
