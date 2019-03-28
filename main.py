# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLabel, QFormLayout, QWidget, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.widget = QWidget()
        self.form = QFormLayout()
        self.selectLbl = QLabel('replace file with ext')
        self.curExt = QTextEdit('.MTS')
        self.toLbl = QLabel('to ext')
        self.destExt = QTextEdit('.mp4')
        self.selectBtn = QPushButton('select')
        self.form.addRow(self.selectLbl, self.curExt)
        self.form.addRow(self.toLbl, self.destExt)
        self.form.addRow(QLabel(), self.selectBtn)
        self.widget.setLayout(self.form)
        self.setCentralWidget(self.widget)

        self.selectBtn.clicked.connect(self.select)

    def select(self):
        fileList, filter_ = QFileDialog.getOpenFileNames(self, 'select files',
                                                         'G:/照片',
                                                         "All Files (*);;Sony Files (*{})".format(
                                                             self.curExt.toPlainText()))
        # print(fileList)
        for f in fileList:
            folder, fullname = os.path.split(f)
            fn, ext = os.path.splitext(fullname)
            destName = fn + self.destExt.toPlainText()
            destFullName = os.path.join(folder, destName)
            print(destFullName)
            os.rename(f, destFullName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

