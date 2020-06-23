#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # position
        self.setGeometry(300, 300, 350, 350)
        # window title
        self.setWindowTitle("Draw path (Paint bezier curve)")
        # show window
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        self.drawCurve(e, p)
        p.end()

    def drawCurve(self, e, p):
        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)

        p.drawPath(path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
