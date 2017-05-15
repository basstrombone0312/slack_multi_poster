# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(563, 470)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.txtIn = QtGui.QTextEdit(self.centralwidget)
        self.txtIn.setGeometry(QtCore.QRect(121, 110, 431, 261))
        self.txtIn.setObjectName(_fromUtf8("txtIn"))
        self.urlBox = QtGui.QLineEdit(self.centralwidget)
        self.urlBox.setGeometry(QtCore.QRect(120, 20, 431, 27))
        self.urlBox.setObjectName(_fromUtf8("urlBox"))
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(351, 390, 201, 51))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 25, 111, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnPost = QtGui.QPushButton(self.centralwidget)
        self.btnPost.setGeometry(QtCore.QRect(120, 390, 201, 51))
        self.btnPost.setObjectName(_fromUtf8("btnPost"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(26, 220, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 67, 71, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.chnBox = QtGui.QLineEdit(self.centralwidget)
        self.chnBox.setGeometry(QtCore.QRect(120, 63, 431, 27))
        self.chnBox.setObjectName(_fromUtf8("chnBox"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnClear.setText(_translate("MainWindow", "クリア", None))
        self.label.setText(_translate("MainWindow", "WebhookURL:", None))
        self.btnPost.setText(_translate("MainWindow", "投稿", None))
        self.label_2.setText(_translate("MainWindow", "投稿内容:", None))
        self.label_3.setText(_translate("MainWindow", "Channels:", None))

