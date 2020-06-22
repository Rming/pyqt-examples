#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFrame
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.color = QColor(0, 0, 0)
        redBtn = QPushButton('Red', self)
        redBtn.setCheckable(True)
        redBtn.move(10, 10)
        redBtn.clicked[bool].connect(self.setColor)

        greenBtn = QPushButton('Green', self)
        greenBtn.setCheckable(True)
        greenBtn.move(10, 60)
        greenBtn.clicked[bool].connect(self.setColor)

        blueBtn = QPushButton('Blue', self)
        blueBtn.setCheckable(True)
        blueBtn.move(10, 110)
        blueBtn.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget {background-color:%s}" % self.color.name())

        # position
        self.setGeometry(300, 300, 350, 150)
        # window title
        self.setWindowTitle("Font Dialog")
        # show window
        self.show()

    def setColor(self, pressed):
        sender = self.sender()
        if pressed:
            val = 255
        else:
            val = 0

        senderText = sender.text()
        if senderText == "Red":
            self.color.setRed(val)
        elif senderText == "Green":
            self.color.setGreen(val)
        elif senderText == "Blue":
            self.color.setBlue(val)

        self.square.setStyleSheet("QWidget {background-color:%s}" % self.color.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
