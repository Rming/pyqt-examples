#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('images/sid.jpg')
        lbl = QLabel()
        lbl.setPixmap(pixmap)
        lbl.move(20, 30)

        hbox = QHBoxLayout(self)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        # position
        self.setGeometry(300, 300, 350, 350)
        # window title
        self.setWindowTitle("Pixmap")
        # show window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
