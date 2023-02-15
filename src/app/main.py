import sys

from PyQt6 import QtWidgets

from src.app.gui.gui import Ui_MainWindow


def start():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    start()
