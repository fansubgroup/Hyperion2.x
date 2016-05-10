# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Fri May  6 14:51:25 2016
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

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(400, 300)
        self.btnAdd = QtGui.QPushButton(dialog)
        self.btnAdd.setGeometry(QtCore.QRect(160, 190, 103, 27))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.IsSave = QtGui.QCheckBox(dialog)
        self.IsSave.setGeometry(QtCore.QRect(160, 250, 102, 24))
        self.IsSave.setObjectName(_fromUtf8("IsSave"))
        self.layoutWidget = QtGui.QWidget(dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 80, 226, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.editAppid = QtGui.QLineEdit(self.layoutWidget)
        self.editAppid.setObjectName(_fromUtf8("editAppid"))
        self.horizontalLayout.addWidget(self.editAppid)
        self.layoutWidget1 = QtGui.QWidget(dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 120, 221, 31))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.editKey = QtGui.QLineEdit(self.layoutWidget1)
        self.editKey.setObjectName(_fromUtf8("editKey"))
        self.horizontalLayout_2.addWidget(self.editKey)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "登录界面", None))
        self.btnAdd.setText(_translate("dialog", "添加", None))
        self.IsSave.setText(_translate("dialog", "记住用户", None))
        self.label.setText(_translate("dialog", "APPID :", None))
        self.label_2.setText(_translate("dialog", "密 钥   :", None))

