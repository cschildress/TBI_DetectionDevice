# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StroopPictures.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QEvent
from PyQt5.QtWidgets import QWidget, QLabel


class Ui_StroopPictures(object):
    count = 0
    quad1 = [None] * 10
    quad2 = [None] * 10
    quad3 = [None] * 10
    quad4 = [None] * 10

    for x in range(1,11):
        quad1[x - 1] = "/home/pi/T" + str(x) + "S1" + ".jpg"
        quad2[x - 1] = "/home/pi/T" + str(x) + "S2" + ".jpg"
        quad3[x - 1] = "/home/pi/T" + str(x) + "S3" + ".jpg"
        quad4[x - 1] = "/home/pi/T" + str(x) + "S4" + ".jpg"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 70, 451, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.image1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.image1.setText("")
        self.image1.setPixmap(QtGui.QPixmap(self.quad1[0]))
        self.image1.setScaledContents(True)
        self.image1.setObjectName("image1")
        self.gridLayout.addWidget(self.image1, 0, 0, 1, 1)
        self.image2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.image2.setText("")
        self.image2.setPixmap(QtGui.QPixmap(self.quad2[0]))
        self.image2.setScaledContents(True)
        self.image2.setObjectName("image2")
        self.gridLayout.addWidget(self.image2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(self.quad3[0]))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.image3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.image3.setText("")
        self.image3.setPixmap(QtGui.QPixmap(self.quad4[0]))
        self.image3.setScaledContents(True)
        self.image3.setObjectName("image3")
        self.gridLayout.addWidget(self.image3, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(290, 0, 201, 51))
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
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600; color:#ff0000;\">ORANGE</span></p></body></html>"))

    def clickable(widget):

        class Filter(QObject):

            clicked = pyqtSignal()
            def eventFilter(self, obj, event):
                if obj == widget:
                    if event.type() == QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            return True
                return False

        filter = Filter(widget)
        widget.installEventFilter
        return filter.clicked

    class Window(QWidget):
        def __init__(self, parent=None):
            QWidget.__init__(self, parent)

            self.clickable(self.image1).connect(self.buildStroop)
            self.clickable(self.image2).connect(self.buildStroop)
            self.clickable(self.image3).connect(self.buildStroop)
            self.clickable(self.image4).connect(self.buildStroop)

    def buildStroop(self):
        self.count += 1
        self.image1.setPixmap(QtGui.QPixmap(self.quad1[self.count]))
        self.image2.setPixmap(QtGui.QPixmap(self.quad2[self.count]))
        self.image3.setPixmap(QtGui.QPixmap(self.quad3[self.count]))
        self.image4.setPixmap(QtGui.QPixmap(self.quad4[self.count]))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_StroopPictures()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
