#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(10, 10)
        ledit = QLineEdit(self)
        ledit.move(10, 100)
        ledit.textChanged[str].connect(self.textChange)

        # position
        self.setGeometry(300, 300, 350, 350)
        # window title
        self.setWindowTitle("Pixmap")
        # show window
        self.show()

    def textChange(self, s):
        self.lbl.setText(s)
        self.lbl.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
