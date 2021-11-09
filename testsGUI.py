from PyQt5.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random, sympy, sys


def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def Test_Ferma(n: int):
    for i in range(1000):
        g = random.randint(2, n - 1)
        if pow(g, n - 1, n) != 1:
            return f'Число <font color="BLUE">{n}</font> <font color="RED"><big>составное</big></font><br>'
    return f'Число <font color="BLUE">{n}</font> вероятно <font color="LIME"><big>простое</big></font><br>'


def Test_SSt(n: int):
    for i in range(1000):
        a = random.randint(2, n - 1)
        g = ((n - 1) // 2)
        r = pow(a, g, n)

        if gcd(a, n) > 1:
            return f'Число <font color="BLUE">{n}</font> <font color="RED"><big>составное</big></font><br>'

        if r != 1 and r != n - 1:
            return f'Число <font color="BLUE">{n}</font> <font color="RED"><big>составное</big></font><br>'

        if r % n != sympy.jacobi_symbol(a, n) % n:
            return f'Число <font color="BLUE">{n}</font> <font color="RED"><big>составное</big></font><br>'

    return f'Число <font color="BLUE">{n}</font> вероятно <font color="LIME"><big>простое</big></font><br>'


def Test_MR(n: int):
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(1000):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return f'Число <font color="BLUE">{n}</font> <font color="RED"><big>составное</big></font><br>'
    return f'Число <font color="BLUE">{n}</font> вероятно <font color="LIME"><big>простое</big></font><br>'


class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.setWindowModality(Qt.NonModal)
        Window.resize(400, 600)
        Window.setMinimumSize(QSize(400, 600))
        Window.setMaximumSize(QSize(400, 600))
        Window.setWindowOpacity(1.000000000000000)
        Window.setLayoutDirection(Qt.LeftToRight)
        Window.setAutoFillBackground(False)
        Window.setStyleSheet(u"QMainWindow\n"
                             "{\n"
                             "	background-color: rgb(230, 230, 230);\n"
                             "	opacity: 0.6;\n"
                             "}")
        Window.setIconSize(QSize(60, 60))
        Window.setAnimated(True)
        Window.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget\n"
                                         "{\n"
                                         "}\n"
                                         "\n"
                                         "QTextBrowser\n"
                                         "{\n"
                                         "	border-top: 5px solid rgb(88, 88, 255);\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox\n"
                                         "{\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox::indicator:unchecked\n"
                                         "{\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "	width: 69px;\n"
                                         "	height: 69px;\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox::indicator:checked\n"
                                         "{\n"
                                         "	border-top: 3px solid rgb(240, 240, 240);\n"
                                         "	border-bottom: 3px solid rgb(240, 240, 240);\n"
                                         "	width:29px;\n"
                                         "	height:29px;\n"
                                         "	margin-left: 20px;\n"
                                         "	margin-right: 20px;\n"
                                         "	background-color: rgb(88, 88, 255);\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox:unchecked:hover\n"
                                         "{\n"
                                         "	background-color: rgb(242, 242, 242);\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox::indicator:unchecked:hover\n"
                                         "{\n"
                                         "	background-color: rgb(242, 242, 242)\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox:checked:hover\n"
                                         "{\n"
                                         "	background-color: rgb(242, 242, 242);\n"
                                         "}")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 350, 400, 250))
        font4 = QFont()
        font4.setFamily(u"Cascadia Code")
        font4.setPointSize(11)
        self.textBrowser.setFont(font4)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QRect(0, 5, 400, 41))
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit.setCursorPosition(0)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 305, 100, 35))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.pushButton.setFont(font1)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(0, 60, 400, 75))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(15)
        self.checkBox.setFont(font2)
        self.checkBox.setStyleSheet(u"")
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(0, 140, 400, 75))
        self.checkBox_2.setFont(font2)
        self.checkBox_2.setStyleSheet(u"")
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(0, 220, 400, 75))
        self.checkBox_3.setFont(font2)
        self.checkBox_3.setStyleSheet(u"")
        Window.setCentralWidget(self.centralwidget)
        self.function()

        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        Window.setWindowTitle("Тестирование на простоту")
        self.pushButton.setText(QCoreApplication.translate("Window", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.checkBox.setText(
            QCoreApplication.translate("Window", u"      \u0424\u0435\u0440\u043c\u0430           ", None))
        self.checkBox_2.setText(QCoreApplication.translate("Window",
                                                           u"\u0421\u043e\u043b\u043e\u0432\u044d\u044f-\u0428\u0442"
                                                           u"\u0440\u0430\u0441\u0441\u0435\u043d\u0430     ",
                                                           None))
        self.checkBox_3.setText(QCoreApplication.translate("Window",
                                                           u"\u041c\u0438\u043b\u043b\u0435\u0440\u0430-\u0420\u0430"
                                                           u"\u0431\u0438\u043d\u0430      ",
                                                           None))

    def function(self):
        self.pushButton.clicked.connect(self.writer)

    def writer(self):
        self.textBrowser.clear()

        if self.lineEdit.text() == '':
            self.textBrowser.append('<h1>Введите число!</h1>')
            return ''

        if self.checkBox.isChecked():
            n = int(self.lineEdit.text())
            self.textBrowser.append(Test_Ferma(n) + '[По тесту Ферма]<br>')

        if self.checkBox_2.isChecked():
            n = int(self.lineEdit.text())
            self.textBrowser.append(Test_Ferma(n) + '[По тесту Соловэя-Штрассена]<br>')

        if self.checkBox_3.isChecked():
            n = int(self.lineEdit.text())
            self.textBrowser.append(Test_Ferma(n) + '[По тесту Миллера-Рабина]<br>')
        self.lineEdit.clear()



app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_Window()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
