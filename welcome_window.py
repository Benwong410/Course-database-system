# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from course_window import Ui_CourseWindow
from timeteable_window import Ui_TimeWindow
import database_model as db


class Ui_MainWindow(object):
    def openWindow(self):
        time = "10:30" ## Todo: function needed to get the current time(import time??)
        weekday = "2"  ## Todo: function needed to get weekday now
        conn = db.connect_db()
        user_id, _, _ = db.get_name_time(conn)
        openCourse = db.get_is_course_start_in_an_hour(conn, user_id, time, weekday)
        if (openCourse):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_CourseWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_TimeWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 424)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 821, 421))
        self.widget.setStyleSheet("background-color:white;\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(120, 160, 591, 71))
        self.label.setStyleSheet("font: 24pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(260, 260, 81, 31))
        self.label_2.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(260, 300, 91, 31))
        self.label_3.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 461, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("assets/woodle_logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(420, 260, 161, 31))
        self.label_5.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(420, 300, 101, 31))
        self.label_6.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.widget , clicked = lambda:self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(340, 350, 113, 32))
        self.pushButton.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(201, 201, 201);\n"
"font: 14pt \".AppleSystemUIFont\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        conn = db.connect_db()
        user_id, name, time = db.get_name_time(conn)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to our Intelligent Course Management System"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_3.setText(_translate("MainWindow", "Login time:"))
        self.label_5.setText(_translate("MainWindow", name))
        self.label_6.setText(_translate("MainWindow", str(time)))

        time = "10:30" ## Todo: function needed to get the current time(import time??)
        weekday = "2"  ## Todo: function needed to get weekday now
        openCourse = db.get_is_course_start_in_an_hour(conn, user_id, time, weekday)

        if (openCourse):
            self.pushButton.setText(_translate("MainWindow", "My Courses"))
        else:
            self.pushButton.setText(_translate("MainWindow", "My Timetable"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
