from PyQt5 import QtCore, QtGui, QtWidgets

import Results


class Ui_Tracing(object):
    count = 0
    line1 = 0
    line2 = 0
    line3 = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.button.setMouseTracking(True)
        self.button.setAutoFillBackground(False)
        self.button.setObjectName("start")
        self.button.setIcon(QtGui.QIcon("/home/pi/pics/tracing1.png"))
        self.button.setIconSize(QtCore.QSize(800, 480))
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
        self.button.released.connect(self.nextWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", ""))

    def nextWindow(self):
        self.count += 1
        if self.count == 1:
            self.button.setIcon(QtGui.QIcon("/home/pi/pics/tracing2.png"))
            self.line1 = 21485
            Results.Ui_Results.line1 = self.line1
        if self.count == 2:
            self.button.setIcon(QtGui.QIcon("/home/pi/pics/tracing3.png"))
            self.line2 = 165834
            Results.Ui_Results.line2 = self.line2
        if self.count > 2:
            self.line3 = 84340
            Results.Ui_Results.line3 = self.line3
            self.launchResults()

    def launchResults(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Results.Ui_Results()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Tracing()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
