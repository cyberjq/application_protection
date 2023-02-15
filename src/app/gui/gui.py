from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow

from src.app import numbers_prime
from src.app.license_checker import LicenseChecker
from src.app.validator import IntValidator


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 450))

        self.widgects = QtWidgets.QStackedWidget(self)

        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralWidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setValidator(IntValidator())
        self.lineEdit.setMaxLength(1000)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.checkButton = QtWidgets.QPushButton(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkButton.setFont(font)
        self.checkButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.checkButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QtWidgets.QFrame(parent=self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.verticalLayout_3.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(1000)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_3.addWidget(self.spinBox)
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setDocumentTitle("")
        self.textEdit.setReadOnly(True)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.generateButton = QtWidgets.QPushButton(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generateButton.setFont(font)
        self.generateButton.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.generateButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.blockLabel = QtWidgets.QLabel(parent=self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.blockLabel.setFont(font)
        self.blockLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.blockLabel.setWordWrap(True)

        self.blockCentralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.blockCentralWidget.setObjectName("centralwidget1")
        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.blockCentralWidget)
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout1.addItem(spacerItem)
        self.horizontalLayout1.addWidget(self.blockLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout1.addItem(spacerItem1)

        self.widgects.addWidget(self.centralWidget)
        self.widgects.addWidget(self.blockCentralWidget)

        MainWindow.setCentralWidget(self.widgects)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkButton.clicked.connect(self.is_prime)
        self.generateButton.clicked.connect(self.generate)
        self.license_checker = LicenseChecker()
        self.license_checker.signal.connect(self.license_handler)
        self.start()


    def start(self):
        self.license_checker.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Простые числа"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите число чтобы проверить на простоту от 2"))
        self.checkButton.setText(_translate("MainWindow", "Проверить"))
        self.label.setText(
            _translate("MainWindow", "Введите количество чисел для генерации простых чисел от 1 до 1000"))
        self.blockLabel.setText(
            _translate("MainWindow", "Программа не активирована!\nАктивируйте программу через активатор!"))
        self.generateButton.setText(_translate("MainWindow", "Сгенерировать"))

    def is_prime(self):
        text = self.lineEdit.text()
        if not text:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Вы не ввели число для проверки!")
            return

        number = int(text)
        if number == 1:
            QtWidgets.QMessageBox.warning(self, "Ошибка", f"Минимальное число для ввода: 2")
            return

        status = numbers_prime.is_prime(number)

        status_text = "Число простое!" if status else "Число составное!"
        QtWidgets.QMessageBox.warning(self, "Информация", status_text)

    def generate(self):
        n = int(self.spinBox.text())
        numbers = numbers_prime.get_random_array(n)
        self.textEdit.setText("\n".join(map(str, numbers)))

    def license_handler(self, license_status: str):
        if license_status == "activated":
            self.widgects.setCurrentIndex(0)
        else:
            self.widgects.setCurrentIndex(1)


