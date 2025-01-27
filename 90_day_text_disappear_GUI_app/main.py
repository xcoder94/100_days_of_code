import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
)
from PySide6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto-Clear Input After Inactivity")

        # Create the QLineEdit (text input field).
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Type something...")

        # Create a QTimer to detect user inactivity.
        self.inactivity_timer = QTimer(self)
        self.inactivity_timer.setInterval(5000)  # 5 seconds (5000 ms)
        self.inactivity_timer.setSingleShot(True)  # Trigger once, then stop
        self.inactivity_timer.timeout.connect(self.clear_text)

        # When the user types (text changes), restart the inactivity timer.
        self.line_edit.textChanged.connect(self.reset_timer)

        # Build a simple layout.
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.line_edit)
        self.setCentralWidget(central_widget)

    def reset_timer(self):
        """
        Stop and restart the timer each time the user types something.
        This means as long as the user keeps typing, the timer never reaches 5s.
        """
        self.inactivity_timer.stop()
        self.inactivity_timer.start()

    def clear_text(self):
        """
        Called when 5 seconds pass without typing in the QLineEdit.
        """
        self.line_edit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())