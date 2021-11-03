# -*- coding: utf-8 -*-

# @Author:Chen Ziang
# @date:2021年10月11日21点59分


import main_ui
import sys
# pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from datetime import *
import os

class mainWindow(QMainWindow,main_ui.Ui_Dialog):
    def __init__(self):
        QMainWindow.__init__(self)
        main_ui.Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.label_2.setText(
            '测试文本'
            '<a href="https://www.baidu.com/>'
            'www,baidu.com</a>'
        )


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    md = mainWindow()
    md.show()
    sys.exit(app.exec_())

