#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ql1 = QLabel("张三", self)
        ql1.move(15, 10)

        ql2 = QLabel("李四", self)
        ql2.move(35, 40)

        ql3 = QLabel("王五", self)
        ql3.move(55, 70)


        # status bar
        self.statusBar().showMessage("Ready")
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("status Bar")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
