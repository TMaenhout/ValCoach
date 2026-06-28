import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import QTimer

from modules.detector.game_detector import GameDetector


class ValCoachApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ValCoach AI")
        self.setMinimumSize(400, 200)

        self.layout = QVBoxLayout()

        self.status_label = QLabel("🔴 Waiting for Valorant...")
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

        self.detector = GameDetector()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)  # check every second

    def update_status(self):
        if self.detector.is_running():
            self.status_label.setText("🟢 Valorant detected")
        else:
            self.status_label.setText("🔴 Waiting for Valorant...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ValCoachApp()
    window.show()
    sys.exit(app.exec())