from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from src.protection import protection
from src.activator.license_checker import LicenseChecker


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 200)
        MainWindow.setMinimumSize(QtCore.QSize(350, 200))
        MainWindow.setMaximumSize(QtCore.QSize(350, 200))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.activateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.activateButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.activateButton.sizePolicy().hasHeightForWidth())
        self.activateButton.setSizePolicy(sizePolicy)
        self.activateButton.setMinimumSize(QtCore.QSize(250, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.activateButton.setFont(font)
        self.activateButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.activateButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.activateButton.clicked.connect(self.activate)
        self.license_checker = LicenseChecker()
        self.license_checker.signal.connect(self.license_handler)
        self.start()

    def start(self):
        self.license_checker.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Активатор"))
        self.activateButton.setText(_translate("MainWindow", "Активировать"))

    def license_handler(self, license_status: str):
        if license_status == "activated":
            self.activateButton.setText("Программа уже активирована!")
            self.activateButton.setEnabled(False)
        else:
            self.activateButton.setText("Активировать")
            self.activateButton.setEnabled(True)

    def activate(self):
        try:
            protection.activate()
            self.license_handler("activated")
            QtWidgets.QMessageBox.information(self, "Информация", "Программа активирована!")
        except OverflowError as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", str(e))
        except FileNotFoundError as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                                          f"Не удалось найти файл: {e.filename}."
                                          f"\nПоложите данный файл в папку с активатором")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Возникла неизвестная ошибка")