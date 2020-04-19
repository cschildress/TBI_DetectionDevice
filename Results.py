# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Results.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Questionnaire, Tracing, StroopPictures

class Ui_MainWindow(object):
    QuestionnaireSum = Questionnaire.sum
    StroopCorrect = StroopPictures.correct
    StroopIncorrect = StroopPictures.incorrect
    StroopTimes = StroopCorrect.times
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(180, 70, 411, 291))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.score1 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.score1.setFont(font)
        self.score1.setObjectName("score1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.score1)
        self.score2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.score2.setFont(font)
        self.score2.setObjectName("score2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.score2)
        self.score3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.score3.setFont(font)
        self.score3.setObjectName("score3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.score3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.result1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.result1.setObjectName("result1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.result1)
        self.result2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.result2.setObjectName("result2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.result2)
        self.result3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.result3.setObjectName("result3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.result3)
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
        self.score1.setText(_translate("MainWindow", "Score 1: " ))
        self.score2.setText(_translate("MainWindow", "Score 2:"))
        self.score3.setText(_translate("MainWindow", "Score 3:"))
        self.result1.setText(_translate("MainWindow", "TextLabel"))
        self.result2.setText(_translate("MainWindow", "TextLabel"))
        self.result3.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
