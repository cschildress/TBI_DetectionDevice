# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StroopPictures.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QEvent
from PyQt5.QtWidgets import QWidget, QLabel
import time
import datetime

import LineTracing
import Results


class Ui_StroopPictures(object):
    count = 0
    matchcount = 0
    nonmatchcount = 0
    correct = 0
    incorrect = 0
    matchcorrect = 0
    matchincorrect = 0
    start = 0
    finish = 0
    diff = 0
    Times = [None] * 5
    MatchTimes = [None] * 5
    quad1 = [None] * 10
    quad2 = [None] * 10
    quad3 = [None] * 10
    quad4 = [None] * 10
    targetColor = ["#dd1fe7", "#6d25d9", "#da2026", "#6d25d9", "#000000", "#d87c48", "#ffcf49", "#1827b7", "#56bc5f"]
    targetName = ["BLUE", "PURPLE", "GREEN", "PURPLE", "YELLOW", "ORANGE", "YELLOW", "RED", "GREEN"]

    for x in range(1, 11):
        quad1[x - 1] = "/home/pi/StroopPictures/T" + str(x) + "S1" + ".jpg"
        quad2[x - 1] = "/home/pi/StroopPictures/T" + str(x) + "S2" + ".jpg"
        quad3[x - 1] = "/home/pi/StroopPictures/T" + str(x) + "S3" + ".jpg"
        quad4[x - 1] = "/home/pi/StroopPictures/T" + str(x) + "S4" + ".jpg"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 70, 401, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(310, 0, 180, 51))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", ""))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                                            "\"><span style=\" font-size:26pt; font-weight:600; color:#4eab5a;\">ORANGE</span></p></body></html>"))
        self.textBrowser.setAutoFillBackground(True)

        self.start = datetime.datetime.now()

        self.pushButton.setIcon(QtGui.QIcon(self.quad1[0]))
        self.pushButton.setIconSize(QtCore.QSize(300, 180))
        self.pushButton.clicked.connect(self.check1)
        self.pushButton.clicked.connect(self.buildStroop)
        self.pushButton.setFlat(True)

        self.pushButton_2.setIcon(QtGui.QIcon(self.quad2[0]))
        self.pushButton_2.setIconSize(QtCore.QSize(300, 180))
        self.pushButton_2.clicked.connect(self.check2)
        self.pushButton_2.clicked.connect(self.buildStroop)
        self.pushButton_2.setFlat(True)

        self.pushButton_3.setIcon(QtGui.QIcon(self.quad3[0]))
        self.pushButton_3.setIconSize(QtCore.QSize(300, 180))
        self.pushButton_3.clicked.connect(self.check3)
        self.pushButton_3.clicked.connect(self.buildStroop)
        self.pushButton_3.setFlat(True)

        self.pushButton_4.setIcon(QtGui.QIcon(self.quad4[0]))
        self.pushButton_4.setIconSize(QtCore.QSize(300, 180))
        self.pushButton_4.clicked.connect(self.check4)
        self.pushButton_4.clicked.connect(self.buildStroop)
        self.pushButton_4.setFlat(True)

    def check1(self):
        self.finish = datetime.datetime.now()

        if self.count == 3:
            self.correct += 1
            self.Times[self.nonmatchcount] = self.finish - self.start
            self.nonmatchcount += 1
        elif self.count == 2 or self.count == 4 or self.count == 6 or self.count == 7 or self.count == 9:
            self.matchincorrect += 1
            self.MatchTimes[self.matchcount] = self.finish - self.start
            self.matchcount += 1
        else:
            self.incorrect += 1
            self.Times[self.nonmatchcount] = self.finish - self.start
            self.nonmatchcount += 1

    def check2(self):
        self.finish = datetime.datetime.now()

        if self.count == 0:
            self.correct += 1
            self.Times[self.nonmatchcount] = self.finish - self.start
            self.nonmatchcount += 1
        elif self.count == 7:
            self.matchcorrect += 1
            self.MatchTimes[self.matchcount] = self.finish - self.start
            self.matchcount += 1
        elif self.count == 2 or self.count == 4 or self.count == 6 or self.count == 9:
            self.matchincorrect += 1
            self.MatchTimes[self.matchcount] = self.finish - self.start
            self.matchcount += 1
        else:
            self.incorrect += 1
            self.Times[self.nonmatchcount] = self.finish - self.start
            self.nonmatchcount += 1

    def check3(self):
        self.finish = datetime.datetime.now()

        if self.count == 1:
            self.correct += 1
            self.Times[self.nonmatchcount] = self.finish - self.start
            self.nonmatchcount += 1
        elif self.count == 2 or self.count == 4 or self.count == 9:
            self.matchcorrect += 1
            self.MatchTimes[self.matchcount] = self.finish - self.start
            self.matchcount += 1
        elif self.count == 6 or self.count == 7:
            self.matchincorrect += 1
            self.MatchTimes[self.matchcount] = self.finish - self.start
            self.matchcount += 1
        else:
            self.incorrect += 1
            self.Times[self.nonmatchcount] = self.finish - self.start
            self.nonmatchcount += 1

    def check4(self):
        self.finish = datetime.datetime.now()

        if self.count == 5:
            self.correct += 1
            self.Times[self.nonmatchcount] = self.finish - self.start
            self.nonmatchcount += 1
        elif self.count == 6:
            self.matchcorrect += 1
            self.MatchTimes[self.matchcount] = self.finish - self.start
            self.matchcount += 1
        elif self.count == 2 or self.count == 4 or self.count == 7 or self.count == 9:
            self.matchincorrect += 1
            self.MatchTimes[self.matchcount] = self.finish - self.start
            self.matchcount += 1
        else:
            self.incorrect += 1
            self.Times[self.nonmatchcount] = self.finish - self.start
            self.nonmatchcount += 1

    def buildStroop(self):
        self.start = datetime.datetime.now()
        if self.count < 9:
            self.count += 1
            self.pushButton.setIcon(QtGui.QIcon(self.quad1[self.count]))
            self.pushButton.setIconSize(QtCore.QSize(326, 196))
            self.pushButton_2.setIcon(QtGui.QIcon(self.quad2[self.count]))
            self.pushButton_2.setIconSize(QtCore.QSize(326, 196))
            self.pushButton_3.setIcon(QtGui.QIcon(self.quad3[self.count]))
            self.pushButton_3.setIconSize(QtCore.QSize(326, 196))
            self.pushButton_4.setIcon(QtGui.QIcon(self.quad4[self.count]))
            self.pushButton_4.setIconSize(QtCore.QSize(326, 196))
            _translate = QtCore.QCoreApplication.translate
            self.textBrowser.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                                                "\"><span style=\" font-size:26pt; font-weight:600; color: "
                                                + self.targetColor[self.count - 1] + "\">" + self.targetName[self.count - 1] + "</span></p></body></html>"))

            #2, 3, 3, 1, 3, 4, 4, 2, 2, 3
        else:
            self.launchTrace()

    def launchTrace(self):
        Results.Ui_Results.StroopCorrect= self.correct
        Results.Ui_Results.StroopIncorrect = self.incorrect
        Results.Ui_Results.StroopMatchCorrect = self.matchcorrect
        Results.Ui_Results.StroopMatchIncorrectCorrect = self.matchincorrect
        self.calcAverages()
        self.window = QtWidgets.QMainWindow()
        self.ui = LineTracing.Ui_LineTracing()
        self.ui.setupUi(self.window)
        self.window.show()

    def calcAverages(self):
        matchSums = 0.0
        for x in range(0,5):
            matchSums += self.MatchTimes[x].seconds + (self.MatchTimes[x].microseconds/1000000)
        matchSums = matchSums/5
        matchSums = "%.2f" % matchSums
        Results.Ui_Results.MatchTimesAvg = matchSums
        nonMatchSums = 0.0
        for x in range(0, 5):
            nonMatchSums += self.Times[x].seconds + (self.Times[x].microseconds / 1000000)
        nonMatchSums = nonMatchSums/5
        nonMatchSums = "%.2f" % nonMatchSums
        Results.Ui_Results.NonMatchTimesAvg = nonMatchSums

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_StroopPictures()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
