import sys

from PyQt6 import QtWidgets

from src.app.gui import UiMainWindow


def start():
    app = QtWidgets.QApplication(sys.argv)
    window = UiMainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    start()
