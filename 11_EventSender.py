#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QPushButton

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('按钮1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('按钮2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.btnClicked)
        btn2.clicked.connect(self.btnClicked)

        # status bar
        self.statusBar().showMessage("Ready")

        # position
        self.setGeometry(300, 300, 250, 150)
        # window title
        self.setWindowTitle("event sender")
        # show window
        self.show()

    def btnClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " was pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
