# -*- coding: utf-8 -*-
"""
感谢https://blog.csdn.net/Mr_Zing/article/details/46945011博文
"""


from PyQt4 import QtCore, QtGui
#从 ui.py 文件里 import ui类
from answer import Ui_Form
import sys
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



#新建自己的窗口类，继承 QDialog 和 ui类
class MyDialog(QtGui.QDialog,Ui_Form):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        #调用内部的 setupUi() ，本身对象作为参数
        self.setupUi(self)
        #连接 QPushButton 的点击信号到槽 BigWork()
        self.BigWork()

    def BigWork(self):
        # 干一件大事... 耗时 10s
       #import 自己的进程类
        from threads import BigWorkThread
        #新建对象
        self.bwThread = BigWorkThread(self.callback)
        #开始执行run()函数里的内容
        self.bwThread.start()

    def callback(self,s):
        # self.label.setText(s)
        pass

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    #新建类对象
    Dialog = MyDialog()
    #显示类对象
    Dialog.show()
    sys.exit(app.exec_())
