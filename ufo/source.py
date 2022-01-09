from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys
import math
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 96, 96))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.shift = 10
        pixmap = QPixmap("ufo.png")
        pixmap = pixmap.scaled(96, 96, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left:
            self.label.move(self.label.x() - self.shift, self.label.y())
        elif event.key() == QtCore.Qt.Key_Right:
            self.label.move(self.label.x() + self.shift, self.label.y())
        elif event.key() == QtCore.Qt.Key_Down:
            self.label.move(self.label.x(), self.label.y() + self.shift)
        elif event.key() == QtCore.Qt.Key_Up:
            self.label.move(self.label.x(), self.label.y() - self.shift)
        if self.label.x() + 96 > self.centralwidget.width():
            self.label.move(0, self.label.y())
        elif self.label.y() + 96 > self.centralwidget.height():
            self.label.move(self.label.x(), 0)
        elif self.label.x() < 0:
            self.label.move(self.centralwidget.width() - 96, self.label.y())
        elif self.label.y() < 0:
            self.label.move(self.label.x(), self.centralwidget.height() - 96)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
