#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QInputDialog, QLineEdit

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Open Dialog', self)
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(130, 22)

        # status bar
        self.statusBar().showMessage("Ready")

        # position
        self.setGeometry(300, 300, 250, 150)
        # window title
        self.setWindowTitle("Input Dialog")
        # show window
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Input your name:")
        if ok:
            self.lineEdit.setText(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
