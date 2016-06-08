#!/usr/bin/python
#coding:utf-8
import Uidlg
import dlglog
import baidu
import sys,os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
Msgbox = QtGui.QMessageBox.about
class logDlg(QtGui.QDialog,dlglog.Ui_dialog):
    def __init__(self,parent=None):
        super(logDlg,self).__init__(parent)
        self.setupUi(self)
        self.IsSave.setChecked(True)
        self.connect(self.btnAdd,QtCore.SIGNAL('clicked()'),self.AddAccount)
    def AddAccount(self):
        if self.editAppid.text()!='' and self.editKey.text()!='':
            self.accept()
        else:
            Msgbox(self,QString("Warning"),QString("Appid or Key is invalid!"))
    def appid(self):
        return self.editAppid.text()
    def key(self):
        return self.editKey.text()
    def isSave(self):
        return self.IsSave.isChecked()



class Dialog(QtGui.QWidget,Uidlg.Ui_Form):
    #appid=''
    #key=''
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        self.setupUi(self)
        self.appid = ''
        self.key=''
        self.src='auto'
        self.dst='zh'
        if os.path.isfile('./Appid'):
            f = open('./Appid','r')
            self.appid=f.readline()
            self.key=f.readline()
            f.close()
            #print self.appid,self.key
            self.lbStatus.setText(QString("Current APPID:")+self.appid)
        self.isSave=False
        self.connect(self.btnBrowser, QtCore.SIGNAL('clicked()'),self.BrowseFile)
        self.connect(self.btnLogin,QtCore.SIGNAL('clicked()'),self.Addappid)
        self.connect(self.btnTranslate,QtCore.SIGNAL('clicked()'),self.Translate)

    def BrowseFile(self):
            #print "btnTest"

        filename = QFileDialog.getOpenFileName(self,QString("Open File"),
                                               QString(''),
                                               QString("SRT FILE (*.srt);;All Files (*)"))
        if filename:
            self.editPath.setText(filename)


    def Addappid(self):
        log=logDlg(parent=self)
        if log.exec_():
            self.appid=log.appid()
            self.key=log.key()
            self.isSave=log.isSave()
            self.lbStatus.setText(QString("Current APPID:")+log.appid())
        log.destroy()
        if self.isSave==True:
            baidu.save_appid(self.appid,self.key)
            print self.appid
            print self.key

    def Translate(self):
        path=self.editPath.text()
        self.src=str(self.srcLang.itemText(self.srcLang.currentIndex()))
        self.dst=str(self.dstLang.itemText(self.dstLang.currentIndex()))
        if os.path.isfile(path):
            if self.appid != '' and self.key != '':
                #print "all is ok!"
                baidu.split_txt(str(path.toUtf8()))
                baidu.translation_txt(self.appid.strip(),self.key.strip(),self.src,self.dst)
                baidu.join_txt()
                baidu.remove_txt()
            else:
                Msgbox(self,"Warning","Please input your APPID at first!")
        else:
            Msgbox(self,"Warning","Please select a srt file at first!")

if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    ui=Dialog()
    ui.show()
    sys.exit(app.exec_())
