# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import time
from answer import Ui_Form
import win32clipboard as w
import win32con
import codecs
import os


#继承 QThread 类
class BigWorkThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    def __init__(self, callback, parent=None):
        super(BigWorkThread, self).__init__(parent)
        self.callback = callback
    #重写 run() 函数，在里面干大事。

    def getSubject(self,s):
        resultLs = []
        may_file = codecs.open('M:\\Users\\MQ\\DeskTop\\may.txt','r','GBK')
        lines = may_file.readlines()
    #     print lines[0]
    #     s = s.decode("GBK")
        for i in range(len(lines)):
    #         print(s)
    #         print lines[i]
            if lines[i].find(s)>0:
                resultLs.append(lines[i])
                resultLs.append(lines[i+1])
                resultLs.append(lines[i+2])
                resultLs.append(lines[i+3])
                resultLs.append(lines[i+4])
                resultLs.append(lines[i+5])
                break
        return resultLs
    def run(self):
        #大事
        print("start...")
        end_time = 60
        start_time = time.time()
        current_time = time.time()
        self.callback("NULL")
        while 1:
            s = "self.getClipboard()"
            # self.callback(s)
            result = "self.getSubject(s)"
            if(len(result)>0):
                self.callback(result[0]+"\n"+result[1]+"\n"+result[2]+"\n"+result[3]+"\n"+result[4]+"\n"+result[5])
            else:
                self.callback('未查询到结果...')
            # while self.cb_ischanged(s):
            #     time.sleep(1)
            current_time = time.time()

        print("end...")
