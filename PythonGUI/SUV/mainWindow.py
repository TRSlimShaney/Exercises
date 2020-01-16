# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exercise2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.trafficControlsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.trafficControlsBox.setGeometry(QtCore.QRect(400, 20, 191, 191))
        self.trafficControlsBox.setObjectName("trafficControlsBox")
        self.redButton = QtWidgets.QPushButton(self.trafficControlsBox)
        self.redButton.setGeometry(QtCore.QRect(50, 30, 111, 29))
        self.redButton.setObjectName("redButton")
        self.yellowButton = QtWidgets.QPushButton(self.trafficControlsBox)
        self.yellowButton.setGeometry(QtCore.QRect(50, 70, 111, 29))
        self.yellowButton.setObjectName("yellowButton")
        self.greenButton = QtWidgets.QPushButton(self.trafficControlsBox)
        self.greenButton.setGeometry(QtCore.QRect(50, 110, 111, 29))
        self.greenButton.setObjectName("greenButton")
        self.leftGreenButton = QtWidgets.QPushButton(self.trafficControlsBox)
        self.leftGreenButton.setGeometry(QtCore.QRect(50, 150, 111, 29))
        self.leftGreenButton.setObjectName("leftGreenButton")
        self.statusBox = QtWidgets.QGroupBox(self.centralwidget)
        self.statusBox.setGeometry(QtCore.QRect(10, 20, 351, 351))
        self.statusBox.setObjectName("statusBox")
        self.trafficLabel = QtWidgets.QLabel(self.statusBox)
        self.trafficLabel.setGeometry(QtCore.QRect(10, 30, 91, 17))
        self.trafficLabel.setObjectName("trafficLabel")
        self.redLabel = QtWidgets.QLabel(self.statusBox)
        self.redLabel.setGeometry(QtCore.QRect(10, 50, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.redLabel.setFont(font)
        self.redLabel.setObjectName("redLabel")
        self.outputList = QtWidgets.QListWidget(self.statusBox)
        self.outputList.setGeometry(QtCore.QRect(10, 100, 331, 241))
        self.outputList.setObjectName("outputList")
        self.yellowLabel = QtWidgets.QLabel(self.statusBox)
        self.yellowLabel.setGeometry(QtCore.QRect(60, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.yellowLabel.setFont(font)
        self.yellowLabel.setObjectName("yellowLabel")
        self.greenLabel = QtWidgets.QLabel(self.statusBox)
        self.greenLabel.setGeometry(QtCore.QRect(140, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.greenLabel.setFont(font)
        self.greenLabel.setObjectName("greenLabel")
        self.leftGreenLabel = QtWidgets.QLabel(self.statusBox)
        self.leftGreenLabel.setGeometry(QtCore.QRect(220, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.leftGreenLabel.setFont(font)
        self.leftGreenLabel.setObjectName("leftGreenLabel")
        self.suvControlsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.suvControlsBox.setGeometry(QtCore.QRect(400, 220, 211, 151))
        self.suvControlsBox.setObjectName("suvControlsBox")
        self.fowardButton = QtWidgets.QPushButton(self.suvControlsBox)
        self.fowardButton.setGeometry(QtCore.QRect(60, 30, 87, 29))
        self.fowardButton.setObjectName("fowardButton")
        self.leftButton = QtWidgets.QPushButton(self.suvControlsBox)
        self.leftButton.setGeometry(QtCore.QRect(10, 70, 87, 29))
        self.leftButton.setObjectName("leftButton")
        self.rightButton = QtWidgets.QPushButton(self.suvControlsBox)
        self.rightButton.setGeometry(QtCore.QRect(110, 70, 87, 29))
        self.rightButton.setObjectName("rightButton")
        self.runOverButton = QtWidgets.QPushButton(self.suvControlsBox)
        self.runOverButton.setGeometry(QtCore.QRect(36, 110, 131, 29))
        self.runOverButton.setObjectName("runOverButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, 10, 21, 371))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SUV"))
        self.trafficControlsBox.setTitle(_translate("MainWindow", "Traffic Controls"))
        self.redButton.setText(_translate("MainWindow", "Red"))
        self.yellowButton.setText(_translate("MainWindow", "Yellow"))
        self.greenButton.setText(_translate("MainWindow", "Green"))
        self.leftGreenButton.setText(_translate("MainWindow", "Left-Turn Green"))
        self.statusBox.setTitle(_translate("MainWindow", "Current Status"))
        self.trafficLabel.setText(_translate("MainWindow", "Traffic Light is:"))
        self.redLabel.setText(_translate("MainWindow", "Red"))
        self.yellowLabel.setText(_translate("MainWindow", "Yellow"))
        self.greenLabel.setText(_translate("MainWindow", "Green"))
        self.leftGreenLabel.setText(_translate("MainWindow", "<---Green"))
        self.suvControlsBox.setTitle(_translate("MainWindow", "SUV Controls"))
        self.fowardButton.setText(_translate("MainWindow", "Forward"))
        self.leftButton.setText(_translate("MainWindow", "Left"))
        self.rightButton.setText(_translate("MainWindow", "Right"))
        self.runOverButton.setText(_translate("MainWindow", "Run Over Ford Pinto"))
