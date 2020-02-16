# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TBI_Detection.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Questionnaire import Ui_Questionnaire

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.beginButton = QtWidgets.QPushButton(self.centralwidget)
        self.beginButton.setGeometry(QtCore.QRect(330, 250, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.beginButton.setFont(font)
        self.beginButton.setObjectName("beginButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(170, 100, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.beginButton.clicked.connect(self.launchQuestionnaire)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.beginButton.setText(_translate("MainWindow", "Begin"))
        self.title.setText(_translate("MainWindow", "Welcome to the TBI Assessment Tool"))

    def launchQuestionnaire(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Questionnaire()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
