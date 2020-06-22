#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox("CheckBox Name", self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        # position
        self.setGeometry(300, 300, 250, 150)
        # window title
        self.setWindowTitle("Font Dialog")
        # show window
        self.show()

    def changeTitle(self, state):
        if state ==  Qt.Checked:
            self.setWindowTitle("CheckBox Checked: Yes")
        else:
            self.setWindowTitle("CheckBox Checked: No")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
