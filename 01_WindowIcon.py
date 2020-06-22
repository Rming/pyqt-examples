#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QDesktopWidget, QToolTip, QToolButton, QPushButton, QApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class exampleQwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 16))
        self.setToolTip("这是一个 Widget")

        btn = QPushButton('退出', self)
        btn.setToolTip("点击按钮退出程序")
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # self.setGeometry(300, 300, 600, 200)
        self.resize(600, 200)
        self.center()

        self.setWindowTitle("ICON 窗口")
        self.setWindowIcon(QIcon("images/logo.png"))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        msg = QMessageBox.question(self, "提示消息", "确认要退出么？", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.No:
            event.ignore()
        else:
            event.accept()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/logo.png"))
    w = exampleQwidget()

    sys.exit(app.exec_())
