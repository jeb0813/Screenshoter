__author__ = 'Administrator'

import sys

# 导入QT,其中包含一些常量，例如颜色等
from PyQt5.QtCore import Qt
# 导入常用组件
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QAction
# 使用调色板等
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate

# 导入项目的py文件
import cza_main_scr_print  # 截图
import cza_main_pic_ppt  # 截图转ppt
# 配置文件
import configparser

# import pandas as pd
import os
import sys
import xlrd
import time
import datetime


# 读取配置文件参数
def read_config():
    global CORP_ID, CORP_SECRET
    # global conn,cursor
    cf = configparser.ConfigParser()
    # cf.read("test.ini")
    cf.read("config.ini", encoding="utf-8-sig")

    CORP_ID = cf.get("qywx", "CORP_ID")
    CORP_SECRET = cf.get("qywx", "CORP_SECRET")
    print(CORP_ID)
    print(CORP_SECRET)
    str_db_ora = cf.get("database_ora", "str_db_ora")


class DemoWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(900, 600)
        # self.WindowMaximized()
        # 获取QMainWindow的MenuBar对象
        bar = self.menuBar()

        # 在menuBar上添加网课截图菜单
        pic_scr = bar.addMenu("网课截图")
        pic_scr_add = pic_scr.addAction("开始截图")
        # staff_up=staff.addAction("更新")

        pic_scr_add.triggered.connect(self.pic_add)
        # staff_file.triggered.connect(self.staff_file)

        # 在menuBar上添加图片变ppt
        checkin = bar.addMenu("图片转ppt")
        checkin_get = checkin.addAction("开始转换")
        # checkin_list=checkin.addAction("清单导出")

        # 在menuBar上添加网课截图菜单
        pic_scr = bar.addMenu("使用说明")
        pic_scr_txt = pic_scr.addAction("截图使用说明")

        # quit = QAction("退出", self)
        # # 文件-->退出，绑定窗口的close槽
        # quit.triggered.connect(self.close)
        # file.addAction(quit)

        # 添加窗口标题
        self.setWindowTitle("网课截图神器  by cza 20210208")

    def pic_add(self):
        self.md = cza_main_scr_print.cza_main_scr_print()
        self.md.show()

    def checkin_get(self):
        print("checkin_get")
        self.md = cza_main_pic_ppt.cza_main_pic_ppt()
        self.md.show()

    def saveProcess(self):
        print("保存")

    def staff_add(self):
        print("add staff")
        # self.md = MainCode()
        # self.md.show()
        self.md = database_t.MainWindow()
        self.md.show()

    def staff_file(self):
        print("staff_file")
        self.md = staff_file_modi.MainCode()
        self.md.show()

    def checkin_list(self):
        print("checkin_list")
        self.md = checkin_list_data.MainCode()
        self.md.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/icon.ico"))
    # 创建一个主窗口
    mainWin = DemoWin()
    # 显示
    mainWin.show()
    # 主循环
    sys.exit(app.exec_())
