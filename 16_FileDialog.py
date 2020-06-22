#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar().showMessage("Ready")

        openFile = QAction(QIcon('images/open_file.png'), '打开文件', self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("选择文件并打开")
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("文件")
        fileMenu.addAction(openFile)

        # position
        self.setGeometry(300, 300, 250, 150)
        # window title
        self.setWindowTitle("Font Dialog")
        # show window
        self.show()

    def showDialog(self):
        fname, ok = QFileDialog.getOpenFileName(self, '打开文件', '/home')
        if fname:
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
