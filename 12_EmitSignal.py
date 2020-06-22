#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QPushButton

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        # status bar
        self.statusBar().showMessage("Ready")

        # position
        self.setGeometry(300, 300, 250, 150)
        # window title
        self.setWindowTitle("emit signal")
        # show window
        self.show()

    def mousePressEvent(self, e):
        # self.close()
        self.c.closeApp.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
