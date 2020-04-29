from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

import Results


class DragMode(object):
    pass


class WindowPos(object):
    pass


class Ui_Tracing(object):
    count = 0
    line1 = 0
    line2 = 0
    line3 = 0
    expectedline = 0
    linedrawn = 0
    startingpoint = 0
    endingpoint = 0
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
        self.button.released.connect(self.mousePressEvent())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", ""))

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if not event.buttons() & Qt.LeftButton:
            return
        # drag detection
        self.drag_mode = self.latent_drag_mode
        if self.drag_mode == DragMode.CLIP_BOX:
            self.clip_box.press_state = self.clip_box.state
        wp = WindowPos.from_QPoint(event.pos())
        self.previous_mouse = wp
        # click detection
        self.maybe_clicking = True
        self.mouse_press_pos = QtCore.QPoint(event.pos().x(), event.pos().y())

    def nextWindow(self):
        self.count += 1
        if self.count == 1:
            self.button.setIcon(QtGui.QIcon("/home/pi/pics/tracing2.png"))
            for x in range(0, 800):
                self.calcpixelDiff()
            Results.Ui_Results.line1 = self.line1
        if self.count == 2:
            self.button.setIcon(QtGui.QIcon("/home/pi/pics/tracing3.png"))
            for x in range(0, 800):
                self.calcpixelDiff()
            Results.Ui_Results.line2 = self.line2
        if self.count > 2:
            for x in range(0, 800):
                self.calcpixelDiff()
            Results.Ui_Results.line3 = self.line3
            self.launchResults()

    def calcpixelDiff(self):
        slope = (self.startingpoint.getY()-self.endingpoint.getY())/(self.startingpoint.getX()-self.endingpoint.getX())
        intercept = slope * self.startingpoint.getX() - self.startingpoint.getY()
        if self.count == 1:
            expectedY = self.mouse_press_pos.x()*slope+intercept
            self.line1 += self.mouse_press_pos.y() - expectedY
        if self.count == 2:
            expectedY = self.mouse_press_pos.x()*slope+intercept
            self.line2 += self.mouse_press_pos.y() - expectedY
        if self.count == 3:
            expectedY = self.mouse_press_pos.x()*slope+intercept
            self.line3 += self.mouse_press_pos.y() - expectedY


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
