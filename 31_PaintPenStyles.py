#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # position
        self.setGeometry(300, 300, 350, 350)
        # window title
        self.setWindowTitle("Paint pen")
        # show window
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.drawLines(e, p)
        p.end()

    def drawLines(self, e, p):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        p.setPen(pen)
        p.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        p.setPen(pen)
        p.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        p.setPen(pen)
        p.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        p.setPen(pen)
        p.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        p.setPen(pen)
        p.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        p.setPen(pen)
        p.drawLine(20, 240, 250, 240)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
