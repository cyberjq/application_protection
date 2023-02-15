import sys

from PyQt6 import QtWidgets

import dotenv

from src.activator.gui import UiMainWindow

dotenv.load_dotenv()


def start():
    app = QtWidgets.QApplication(sys.argv)
    window = UiMainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    start()
