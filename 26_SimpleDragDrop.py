#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())
        self.adjustSize()


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ledit = QLineEdit(self)
        ledit.setText("输入文字，选择并拖拽到按钮")
        ledit.adjustSize()
        ledit.setDragEnabled(True)
        ledit.move(30, 65)

        btn = Button("Button", self)
        btn.move(190, 65)

        # position
        self.setGeometry(300, 300, 350, 350)
        # window title
        self.setWindowTitle("simple drag and drop")
        # show window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
