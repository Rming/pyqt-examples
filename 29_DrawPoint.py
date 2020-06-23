#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = "你好, Qt5"
        # position
        self.setGeometry(300, 300, 350, 350)
        # window title
        self.setWindowTitle("Drawing text")
        # show window
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.drawPoints(e, p)
        p.end()

    def drawPoints(self, e, p):
        # p.setPen(QColor(168, 34, 3))
        p.setPen(Qt.red)
        size = self.size()
        if size.height() <= 1 or self.width() <= 1:
            return

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            p.drawPoint(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
