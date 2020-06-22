#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QFrame, QColorDialog, QLineEdit
from PyQt5.QtGui import QColor

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Open Dialog', self)
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)

        color = QColor(0, 0, 0)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget {background-color: %s}" % color.name())
        self.frm.setGeometry(130, 22, 100, 100)

        # status bar
        self.statusBar().showMessage("Ready")

        # position
        self.setGeometry(300, 300, 250, 150)
        # window title
        self.setWindowTitle("Color Dialog")
        # show window
        self.show()

    def showDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.frm.setStyleSheet("QWidget {background-color: %s}" % color.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
