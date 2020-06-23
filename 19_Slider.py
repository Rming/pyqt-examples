#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("images/mute.png"))
        self.label.setGeometry(160, 40, 80, 30)

        # position
        self.setGeometry(300, 300, 350, 150)
        # window title
        self.setWindowTitle("Slider")
        # show window
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap("images/mute.png"))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap("images/min.png"))
        elif 30 < value <= 80:
            self.label.setPixmap(QPixmap("images/med.png"))
        else:
            self.label.setPixmap(QPixmap("images/max.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
