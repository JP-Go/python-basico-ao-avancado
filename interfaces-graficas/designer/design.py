# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.BtnFindFile = QtWidgets.QPushButton(self.centralwidget)
        self.BtnFindFile.setObjectName("BtnFindFile")
        self.gridLayout.addWidget(self.BtnFindFile, 1, 5, 1, 1)
        self.HeightPropValue = QtWidgets.QLineEdit(self.centralwidget)
        self.HeightPropValue.setObjectName("HeightPropValue")
        self.gridLayout.addWidget(self.HeightPropValue, 2, 4, 1, 1)
        self.HeightPropLabel = QtWidgets.QLabel(self.centralwidget)
        self.HeightPropLabel.setObjectName("HeightPropLabel")
        self.gridLayout.addWidget(self.HeightPropLabel, 2, 3, 1, 1)
        self.InputImgPath = QtWidgets.QLineEdit(self.centralwidget)
        self.InputImgPath.setObjectName("InputImgPath")
        self.gridLayout.addWidget(self.InputImgPath, 1, 0, 1, 5)
        self.WidthPropLabel = QtWidgets.QLabel(self.centralwidget)
        self.WidthPropLabel.setObjectName("WidthPropLabel")
        self.gridLayout.addWidget(self.WidthPropLabel, 2, 0, 1, 1)
        self.BtnResize = QtWidgets.QPushButton(self.centralwidget)
        self.BtnResize.setObjectName("BtnResize")
        self.gridLayout.addWidget(self.BtnResize, 2, 5, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 713, 407))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ImgPlaceholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ImgPlaceholder.setText("")
        self.ImgPlaceholder.setObjectName("ImgPlaceholder")
        self.gridLayout_2.addWidget(self.ImgPlaceholder, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 7)
        self.BtnSaveFile = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSaveFile.setObjectName("BtnSaveFile")
        self.gridLayout.addWidget(self.BtnSaveFile, 3, 5, 1, 1)
        self.WidthPropValue = QtWidgets.QLineEdit(self.centralwidget)
        self.WidthPropValue.setObjectName("WidthPropValue")
        self.gridLayout.addWidget(self.WidthPropValue, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redimensionar Imagem"))
        self.BtnFindFile.setText(_translate("MainWindow", "&Find..."))
        self.HeightPropLabel.setText(_translate("MainWindow", "Height"))
        self.WidthPropLabel.setText(_translate("MainWindow", "Width"))
        self.BtnResize.setText(_translate("MainWindow", "&Resize"))
        self.BtnSaveFile.setText(_translate("MainWindow", "&Save..."))
