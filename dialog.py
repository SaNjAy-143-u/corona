# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 258)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 55, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 55, 16))
        self.label_3.setObjectName("label_3")

        self.lineEdit_lat = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_lat.setGeometry(QtCore.QRect(120, 90, 113, 22))
        self.lineEdit_lat.setObjectName("lineEdit")

        self.lineEdit_long = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_long.setGeometry(QtCore.QRect(120, 150, 113, 22))
        self.lineEdit_long.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 80, 160, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.radioButton_N = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_N.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_N)

        self.radioButton_S = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_S.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton_S)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(260, 140, 160, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.radioButton_W = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_W.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_W)

        self.radioButton_E = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_E.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_E)

        self.retranslateUi(Dialog)

        self.pushButton.clicked.connect(self.button_ok)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def button_ok(self):
        global lat, long
        if self.radioButton_N.isChecked():
            lat = self.lineEdit_lat.text() + "N"
        else:
            lat = self.lineEdit_lat.text() + "S"

        if self.radioButton_W.isChecked():
            long = self.lineEdit_long.text() + "W"
        else:
            long = self.lineEdit_long.text() + "E"

        print(lat, long)
        Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter lat/long for this point :-"))
        self.label_2.setText(_translate("Dialog", "Latitude"))
        self.label_3.setText(_translate("Dialog", "Longitude"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.radioButton_N.setText(_translate("Dialog", "N"))
        self.radioButton_S.setText(_translate("Dialog", "S"))
        self.radioButton_W.setText(_translate("Dialog", "W"))
        self.radioButton_E.setText(_translate("Dialog", "E"))
