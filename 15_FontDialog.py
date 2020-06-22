#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QFontDialog, QSizePolicy, QVBoxLayout
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        btn = QPushButton('Open Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)
        vbox.addWidget(btn)

        self.lb = QLabel("Knowledge only matters", self)
        self.lb.move(130, 20)
        vbox.addWidget(self.lb)


        # position
        self.setGeometry(300, 300, 250, 150)
        # window title
        self.setWindowTitle("Font Dialog")
        # show window
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lb.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
