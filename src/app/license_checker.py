import time

from PyQt6 import QtCore

from src.protection import protection


class LicenseChecker(QtCore.QThread):

    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        while True:
            try:
                if protection.is_activated():
                    self.signal.emit("activated")
                else:
                    self.signal.emit("no activated")

            except Exception as e:
                self.signal.emit("no activated")
            finally:
                time.sleep(60)
