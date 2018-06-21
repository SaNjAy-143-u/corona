# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easy.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 275)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel.setGeometry(QtCore.QRect(30, 60, 151, 16))
        self.inputLabel.setObjectName("label")

        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(30, 110, 161, 16))
        self.outputLabel.setObjectName("label_2")

        self.inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(210, 50, 401, 31))
        self.inputText.setObjectName("lineEdit")

        self.outputText = QtWidgets.QLineEdit(self.centralwidget)
        self.outputText.setGeometry(QtCore.QRect(210, 100, 401, 31))
        self.outputText.setObjectName("lineEdit_3")

        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(340, 180, 93, 28))
        self.next.setObjectName("pushButton")

        self.browseInput = QtWidgets.QPushButton(self.centralwidget)
        self.browseInput.setGeometry(QtCore.QRect(640, 50, 93, 28))
        self.browseInput.setObjectName("pushButton_2")

        self.browseOutput = QtWidgets.QPushButton(self.centralwidget)
        self.browseOutput.setGeometry(QtCore.QRect(640, 100, 93, 28))
        self.browseOutput.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        self.browseInput.clicked.connect(self.openFileNameDialog)
        self.browseOutput.clicked.connect(self.openFolderNameDialog)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CORONA IP"))
        self.inputLabel.setText(_translate("MainWindow", "Enter input image location "))
        self.outputLabel.setText(_translate("MainWindow", "Enter output image location"))
        self.next.setText(_translate("MainWindow", "NEXT"))
        self.browseInput.setText(_translate("MainWindow", "Browse"))
        self.browseOutput.setText(_translate("MainWindow", "Browse"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def openFileNameDialog(self):

        fileName = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QWidget(), 'Browse file', 'C:\\',
                                                   "corona image file (*.tif)")

        self.inputText.setText(fileName[0])

    def openFolderNameDialog(self):

        folderName = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QWidget(), "Select Directory")

        self.outputText.setText(folderName)


def inputWindow():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

