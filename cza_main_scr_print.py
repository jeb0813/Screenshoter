__author__ = 'cza'

import sys
# pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
# 界面
import cza_scr_print

from pynput.keyboard import Listener
import logging
from PIL import ImageGrab

from datetime import *
import time


class cza_main_scr_print(QMainWindow, cza_scr_print.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        cza_scr_print.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.textEdit.append('欢迎使用本软件.....')
        self.textEdit.append('程序开始运行...........')

        # self.pushButton.clicked.connect(self.on_open_save_dir)
        self.toolButton.clicked.connect(self.on_open_save_dir)
        self.pushButton_2.clicked.connect(self.on_scr_print)

    #
    def on_open_save_dir(self):
        print('on_open_save_dir')
        FullSave_dir = QFileDialog.getExistingDirectory(self)
        if len(FullSave_dir) > 0:
            self.lineEdit.setText(FullSave_dir)
            print(FullSave_dir)
            self.textEdit.append('生成文件保存目录为：' + FullSave_dir)

    def on_scr_print(self):
        print("on_scr_print")
        FullSave_dir = self.lineEdit.text()
        if FullSave_dir == '':
            QMessageBox.warning(self, "出错了！", "未选择图片保存目录", QMessageBox.Yes)
        else:
            self.textEdit.append('开始截屏.......')
            with Listener(on_press=self.press, on_release=self.on_release) as listener:
                listener.join()

    def on_release(self, key):
        pass
        # print('esc')

    def press(self, key):
        logging.info(key)
        print(key, type(key))
        # print(key.char)
        print(str(key))

        if str(key) == "Key.print_screen":
            print("打印屏幕")
            self.screen_print()

        if str(key) == "Key.esc":
            print("退出")
            return False

    def add_edit(self, nr):
        self.textEdit.append('ddd')
        self.textEdit.append(nr)

    def screen_print(self):

        im = ImageGrab.grab()
        dt = datetime.now()
        FullSave_dir = self.lineEdit.text()
        filename = FullSave_dir + "/scr_pic_" + dt.strftime('%Y%m%d%H%M%S') + '.png'
        print(filename)
        self.textEdit.append('成功生成图片：' + filename)
        im.save(filename)


#
# def press(key):
#     logging.info(key)
#     print(key,type(key))
#     #print(key.char)
#     print(str(key))
#
#     if str(key)=="Key.print_screen":
#         print("打印屏幕")
#         screen_print()
#
#     if str(key)=="Key.esc":
#         print("退出")
#         listener.stop()
#         #screen_print()
#
# def screen_print1():
#     im = ImageGrab.grab()
#     dt=datetime.now()
#     filename="screen_pic_"+dt.strftime( '%Y%m%d%H%M%S')+'.png'
#     im.save(filename)
#


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    md = cza_main_scr_print()
    md.show()
    sys.exit(app.exec_())
