import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt


class PowerMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showFullScreen()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)
        buttons = [
            ("", "systemctl poweroff"),
            ("", "systemctl reboot"),
            ("", "systemctl suspend"),
            ("", "hyprlock"),
            ("", "hyprctl session exit"),
        ]

        for text, cmd in buttons:
            btn = QPushButton(text)
            btn.setObjectName("button")
            btn.setFixedSize(160, 160)
            btn.clicked.connect(lambda _, c=cmd: self.execute_command(c))
            btn.setDefault(True)
            layout.addWidget(btn)

        self.load_stylesheet("styles.css")

    def execute_command(self, command):
        subprocess.run(command, shell=True)
        self.close()

    def load_stylesheet(self, path):
        try:
            with open(path, "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"Missing styles.css file.")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PowerMenu()
    window.show()
    sys.exit(app.exec())
