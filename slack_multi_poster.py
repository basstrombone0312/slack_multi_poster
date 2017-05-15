#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from slack_post import *
import design
 
class MainWin(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        f = open("webhook.txt", 'r')
        self.urlBox.setText(f.read())
        f.close()
 
    #投稿ボタン押した時
    def doPost(self, value):
        url = self.urlBox.text()
        channel = self.chnBox.text()
        text = self.txtIn.toPlainText()
        slack_post(url, channel, text)
        f = open("webhook.txt", 'w')
        f.write(url)
        f.close()        
        self.txtIn.clear()
        self.chnBox.clear()

    #クリアボタン押した時 
    def doClear(self, value):
        self.txtIn.clear()
 
def main():
    app = QtGui.QApplication(sys.argv)
    form = MainWin()
    form.show()

    #投稿ボタン
    form.btnPost.clicked.connect(form.doPost)
    #クリアボタン
    form.btnClear.clicked.connect(form.doClear)

    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
