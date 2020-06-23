#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # position
        self.setGeometry(300, 300, 350, 350)
        # window title
        self.setWindowTitle("Paint brush styles")
        # show window
        self.show()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.drawBrushes(e, p)
        p.end()

    def drawBrushes(self, e, p):
        brush = QBrush(Qt.SolidPattern)
        p.setBrush(brush)
        p.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        p.setBrush(brush)
        p.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        p.setBrush(brush)
        p.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.DiagCrossPattern)
        p.setBrush(brush)
        p.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        p.setBrush(brush)
        p.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        p.setBrush(brush)
        p.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        p.setBrush(brush)
        p.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        p.setBrush(brush)
        p.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        p.setBrush(brush)
        p.drawRect(250, 195, 90, 60)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
