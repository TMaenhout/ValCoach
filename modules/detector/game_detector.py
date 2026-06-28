import psutil


class GameDetector:
    def __init__(self):
        self.process_name = "VALORANT-Win64-Shipping.exe"

    def is_running(self):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == self.process_name:
                return True
        return False