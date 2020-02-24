# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestionnaireWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Questionnaire(object):

    questionCount = 0
    sum = 0
    questions = ["I know my name and what day of the week it is.",
                 "I know where I am and why I am here.",
                 "I can remember the incident clearly."
                 "I have felt nauseous or vomited since the incident.",
                 "I feel week, drowsy, or tired right now.",
                 "My ears have been ringing since the incident.",
                 "I have increased sensitivity to light and noise since the incident",
                 "I have blurry visual or trouble focusing on objects.",
                 "I have had difficulty with coordination or movement since the incident.",
                 "I feel more irritable than usual."]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(315, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(200, 120, 399, 121))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.instructions_1 = QtWidgets.QLabel(self.centralwidget)
        self.instructions_1.setGeometry(QtCore.QRect(200, 60, 761, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instructions_1.setFont(font)
        self.instructions_1.setObjectName("instructions_1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 270, 702, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_0.sizePolicy().hasHeightForWidth())
        self.radioButton_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_0.setFont(font)
        self.radioButton_0.setObjectName("radioButton_0")
        self.horizontalLayout.addWidget(self.radioButton_0)
        self.radioButton_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.horizontalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.group = QtWidgets.QButtonGroup()
        self.group.addButton(self.radioButton_0)
        self.group.addButton(self.radioButton_1)
        self.group.addButton(self.radioButton_2)
        self.group.addButton(self.radioButton_3)
        self.group.addButton(self.radioButton_4)

        self.pushButton.clicked.connect(self.buildQuestion)
        if self.questionCount == 10:
            print(self.sum)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Questionnaire"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Question 1: </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Do you have any problems remembering the incident?</span></p></body></html>"))
        self.radioButton_0.setText(_translate("MainWindow", "Strongly Disagree"))
        self.radioButton_1.setText(_translate("MainWindow", "Disagree"))
        self.radioButton_2.setText(_translate("MainWindow", "Neutral"))
        self.radioButton_3.setText(_translate("MainWindow", "Agree"))
        self.radioButton_4.setText(_translate("MainWindow", "Strongly Agree"))
        self.pushButton.setText(_translate("MainWindow", "Next ->"))
        self.instructions_1.setText(_translate("MainWindow", "The following questions are to be answered by the \n                patient to the best of their ability."))

    def buildQuestion(self):
        if self.questionCount < 9:
            if self.radioButton_0.isChecked():
                self.sum += 0
            elif self.radioButton_1.isChecked():
                self.sum += 1
            elif self.radioButton_2.isChecked():
                self.sum += 2
            elif self.radioButton_3.isChecked():
                self.sum += 3
            elif self.radioButton_4.isChecked():
                self.sum += 4
            self.questionCount += 1
            self.textBrowser_2.clear()
            _translate = QtCore.QCoreApplication.translate

            self.textBrowser_2.setHtml(_translate("MainWindow",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Question " + str(self.questionCount + 1) + ": </span></p>\n"
                                                  "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">" + self.questions[self.questionCount - 1] + "</span></p></body></html>"))
            self.group.setExclusive(False)
            self.radioButton_0.setChecked(False)
            self.radioButton_1.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(False)
            self.group.setExclusive(True)
        else:
            if self.radioButton_0.isChecked():
                self.sum += 0
            elif self.radioButton_1.isChecked():
                self.sum += 1
            elif self.radioButton_2.isChecked():
                self.sum += 2
            elif self.radioButton_3.isChecked():
                self.sum += 3
            elif self.radioButton_4.isChecked():
                self.sum += 4
            self.pushButton.clicked.connect(self.launchStroop)

    def launchStroop(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StroopTest()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Questionnaire()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
