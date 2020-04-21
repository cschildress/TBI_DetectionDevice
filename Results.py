from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Results(object):
    QuestionnaireSum = 0
    StroopCorrect = 0
    StroopIncorrect = 0
    StroopMatchCorrect = 0
    StroopMatchIncorrect = 0
    MatchTimesAvg = 0.0
    NonMatchTimesAvg = 0.0
    count = 0
    line1 = 0
    line2 = 0
    line3 = 0
    lowtest = 0
    midtest = 0
    hightest = 0
    finalresult = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 781, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.testLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.testLabel.setFont(font)
        self.testLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.testLabel.setAutoFillBackground(False)
        self.testLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.testLabel.setObjectName("testLabel")
        self.verticalLayout.addWidget(self.testLabel)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 400, 779, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
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
        if self.count < 2:
            self.pushButton.clicked.connect(self.changeWindow)
        else:
            self.pushButton.clicked.connect()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testLabel.setText(_translate("MainWindow", "Questionnaire Results:"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Stroop Results ->"))
        self.changeWindow()

    def changeWindow(self):
        _translate = QtCore.QCoreApplication.translate
        if self.count == 0:
            font = QtGui.QFont()
            font.setPointSize(15)
            self.label.setFont(font)
            self.label.setText(_translate("MainWindow", "- You scored "
                                            + str(self.QuestionnaireSum) + " out of 40."))
            if self.QuestionnaireSum < 5:
                self.lowtest += 1
                self.label_2.setPixmap(QtGui.QPixmap("/home/pi/pics/questionnaireResults1.JPG"))
            if self.QuestionnaireSum > 5 and self.QuestionnaireSum < 15:
                self.midtest += 1
                self.finalresult += 2
                self.label_2.setPixmap(QtGui.QPixmap("/home/pi/pics/questionnaireResults2.JPG"))
            if self.QuestionnaireSum > 15:
                self.hightest += 1
                self.finalresult += 4
                self.label_2.setPixmap(QtGui.QPixmap("/home/pi/pics/questionnaireResults3.JPG"))
        if self.count == 1:
            self.pushButton.setText(_translate("MainWindow", "Line Tracing Results ->"))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label.setFont(font)
            self.testLabel.setText(_translate("MainWindow", "Stroop Test Results:"))
            self.label.setText(_translate("MainWindow", "Color and Name Matching:\n- You scored "
                                        + str(self.StroopMatchCorrect) + " out of 5. \n- With an average"
                                        " time of " + str(self.MatchTimesAvg) + " seconds."
                                        + "\n\nColor and Name NOT Matching\n- You scored "
                                        + str(self.StroopCorrect) + " out of 5. \n- With an average"
                                        " time of " + str(self.NonMatchTimesAvg) + " seconds."))
            self.label_2.setScaledContents(True)
            self.lowtest += 1
            self.label_2.setPixmap(QtGui.QPixmap("/home/pi/pics/stroopResults.JPG"))
        if self.count == 2:
            self.pushButton.setText(_translate("MainWindow", "Final Results"))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label.setFont(font)
            self.testLabel.setText(_translate("MainWindow", "Line Tracing Test Results:"))
            avg = (self.line1 + self.line2 + self.line3)/3
            self.label.setText(_translate("MainWindow", "Line 1: " + str(self.line1) + " pixel differential \nLine 2: "
                                          + str(self.line2) + " pixel differential \nLine 3: " + str(self.line3) + " pixel differential"
                                          "\nYour average pixel differential is " + str(avg) + "."))
            self.label_2.setScaledContents(False)
            if avg < 30000:
                self.lowtest += 1
                self.label_2.setPixmap(QtGui.QPixmap("/home/pi/pics/tracingResult1.JPG"))
            if avg > 30000 and avg < 60000:
                self.midtest += 1
                self.finalresult += 2
                self.label_2.setPixmap(QtGui.QPixmap("/home/pi/pics/tracingResult2.JPG"))
            if avg > 60000:
                self.hightest += 1
                self.finalresult += 4
                self.label_2.setPixmap(QtGui.QPixmap("/home/pi/pics/tracingResult3.JPG"))
        if self.count == 3:
            self.pushButton.setText(_translate("MainWindow", "End Program"))
            self.testLabel.setText(_translate("MainWindow", "Final Results:"))
            self.label_2.setText(_translate("MainWindow", " "))
            font = QtGui.QFont()
            font.setPointSize(25)
            self.label.setFont(font)
            if self.finalresult < 4:
                self.label.setText(_translate("MainWindow", "\nNumber of Low Risk Results: " + str(self.lowtest) +
                                            "\n\nNumber of Medium Risk Results: " + str(self.midtest) +
                                            "\n\nNumber of High Risk Results: " + str(self.hightest)))
            else:
                self.label.setText(_translate("MainWindow", "\nNumber of Low Risk Results: " + str(self.lowtest) +
                                              "\n\nNumber of Medium Risk Results: " + str(self.midtest) +
                                              "\n\nNumber of High Risk Results: " + str(self.hightest) +
                                              "\n\nYour tests have concerning results,\nyou should visit a doctor"
                                              "for the possibility of a mild traumatic brain injury"))

        if self.count == 4:
            exit()
        self.count += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Results()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
