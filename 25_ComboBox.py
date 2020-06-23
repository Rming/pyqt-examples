#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QComboBox


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)
        combo.activated[str].connect(self.onActivated)

        # position
        self.setGeometry(300, 300, 350, 350)
        # window title
        self.setWindowTitle("ComboBox")
        # show window
        self.show()

    def onActivated(self, s):
        self.lbl.setText(s)
        self.lbl.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
