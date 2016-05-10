# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri May  6 16:29:42 2016
#      by: PyQt4 UI code generator 4.10.4
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
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 61, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.editPath = QtGui.QLineEdit(Form)
        self.editPath.setGeometry(QtCore.QRect(90, 30, 181, 29))
        self.editPath.setObjectName(_fromUtf8("editPath"))
        self.btnBrowser = QtGui.QPushButton(Form)
        self.btnBrowser.setGeometry(QtCore.QRect(280, 30, 81, 27))
        self.btnBrowser.setObjectName(_fromUtf8("btnBrowser"))
        self.dstLang = QtGui.QComboBox(Form)
        self.dstLang.setGeometry(QtCore.QRect(250, 111, 91, 31))
        self.dstLang.setObjectName(_fromUtf8("dstLang"))
        self.dstLang.addItem(_fromUtf8(""))
        self.dstLang.addItem(_fromUtf8(""))
        self.dstLang.addItem(_fromUtf8(""))
        self.dstLang.addItem(_fromUtf8(""))
        self.dstLang.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 118, 72, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.srcLang = QtGui.QComboBox(Form)
        self.srcLang.setGeometry(QtCore.QRect(30, 112, 131, 31))
        self.srcLang.setObjectName(_fromUtf8("srcLang"))
        self.srcLang.addItem(_fromUtf8(""))
        self.srcLang.addItem(_fromUtf8(""))
        self.srcLang.addItem(_fromUtf8(""))
        self.srcLang.addItem(_fromUtf8(""))
        self.srcLang.addItem(_fromUtf8(""))
        self.srcLang.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 72, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(260, 90, 72, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lbStatus = QtGui.QLabel(Form)
        self.lbStatus.setGeometry(QtCore.QRect(0, 268, 411, 31))
        self.lbStatus.setObjectName(_fromUtf8("lbStatus"))
        self.btnTranslate = QtGui.QPushButton(Form)
        self.btnTranslate.setGeometry(QtCore.QRect(150, 170, 103, 27))
        self.btnTranslate.setObjectName(_fromUtf8("btnTranslate"))
        self.btnLogin = QtGui.QPushButton(Form)
        self.btnLogin.setGeometry(QtCore.QRect(150, 220, 103, 27))
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "字幕翻译工具", None))
        self.label.setText(_translate("Form", "路径:", None))
        self.btnBrowser.setText(_translate("Form", "浏览", None))
        self.dstLang.setItemText(0, _translate("Form", "zh", None))
        self.dstLang.setItemText(1, _translate("Form", "en", None))
        self.dstLang.setItemText(2, _translate("Form", "jp", None))
        self.dstLang.setItemText(3, _translate("Form", "kor", None))
        self.dstLang.setItemText(4, _translate("Form", "th", None))
        self.label_2.setText(_translate("Form", "       - ->", None))
        self.srcLang.setItemText(0, _translate("Form", "auto", None))
        self.srcLang.setItemText(1, _translate("Form", "en", None))
        self.srcLang.setItemText(2, _translate("Form", "zh", None))
        self.srcLang.setItemText(3, _translate("Form", "jp", None))
        self.srcLang.setItemText(4, _translate("Form", "kor", None))
        self.srcLang.setItemText(5, _translate("Form", "th", None))
        self.label_3.setText(_translate("Form", "源语言", None))
        self.label_4.setText(_translate("Form", "目标语言", None))
        self.lbStatus.setText(_translate("Form", "当前状态:未添加APPID", None))
        self.btnTranslate.setText(_translate("Form", "一键翻译", None))
        self.btnLogin.setText(_translate("Form", "添加APPID", None))

