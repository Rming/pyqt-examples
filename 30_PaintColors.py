#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # position
        self.setGeometry(300, 300, 350, 350)
        # window title
        self.setWindowTitle("Paint colors")
        # show window
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.drawRect(e, p)
        p.end()

    def drawRect(self, e, p):
        color = QColor(0, 0, 0)
        color.setNamedColor('#00F')
        p.setPen(color)

        p.setBrush(QColor(200, 0, 0))
        p.drawRect(10, 15, 90, 60)

        p.setBrush(QColor(255, 80, 0, 160))
        p.drawRect(130, 15, 90, 60)

        p.setBrush(QColor(25, 0, 90, 200))
        p.drawRect(250, 15, 90, 60)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
