import sys

from PyQt6 import QtWidgets

import dotenv

from src.activator.gui.gui import Ui_MainWindow

dotenv.load_dotenv()


def start():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    start()
