# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Answer.ui'
#
# Created: Tue May 15 17:26:32 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(900, 420)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 70, 70))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(790, 50, 70, 70))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 290, 90, 90))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bernard MT Condensed"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        poker_t ='2jjjd999988654444'
        for i in range(len(poker_t)):
            self.label_4 = QtGui.QLabel(Dialog)
            self.label_5 = QtGui.QLabel(Dialog)
            self.label_4.setGeometry(QtCore.QRect(150+i*30, 260, 30, 120))
            self.label_5.setGeometry(QtCore.QRect(154+i*30, 227, 30, 120))
            self.label_4.setObjectName(_fromUtf8("label_4"))
            self.label_4.setPixmap(QtGui.QPixmap('./poke_p.png'))
            self.label_5.setFont(font)
            self.label_5.setText(_translate("Form", getPokerCharacter(poker_t[i]), None))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setPixmap(QtGui.QPixmap('./peasant2.png'))
        self.label_2.setPixmap(QtGui.QPixmap('./peasant.png'))
        self.label_3.setPixmap(QtGui.QPixmap('./me.gif'))
    
def getPokerCharacter(s):
    if s == 'd':
        return '10'
    elif s == 'w':
        return 'Joker'
    elif s == 'o':
        return 'joker'
    else:
        return s.upper()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
