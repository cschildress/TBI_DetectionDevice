# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tracing.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tracing(object):
    count = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(50, 40, 41, 41))
        self.startButton.setMouseTracking(True)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setObjectName("")
        self.startButton.setIcon(QtGui.QIcon("/Users/CABOOMDUDE23/Downloads/PythonStuff/number1.png"))
        self.startButton.setIconSize(QtCore.QSize(41, 41))
        self.endButton = QtWidgets.QPushButton(self.centralwidget)
        self.endButton.setGeometry(QtCore.QRect(700, 370, 41, 41))
        self.endButton.setMouseTracking(True)
        self.endButton.setAutoFillBackground(False)
        self.endButton.setObjectName("")
        self.endButton.setIcon(QtGui.QIcon("/Users/CABOOMDUDE23/Downloads/PythonStuff/number2.JPEG"))
        self.endButton.setIconSize(QtCore.QSize(41, 41))
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

        #self.startButton.clicked.connect(self.mouseStart())
        self.endButton.released.connect(self.nextWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", ""))
        self.endButton.setText(_translate("MainWindow", ""))

    def nextWindow(self):
        self.count += 1
        print("button released")
        if self.count > 2:
            print("done with testing")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Tracing()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
