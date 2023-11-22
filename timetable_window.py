# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timetable_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import database_model as db

class Ui_CourseWindow(object):
    def setupUi(self, CourseWindow):
        CourseWindow.setObjectName("CourseWindow")
        CourseWindow.resize(844, 743)
        self.centralwidget = QtWidgets.QWidget(CourseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 841, 791))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 839, 789))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 841, 801))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 461, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("assets/woodle_logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 180, 841, 41))
        self.lineEdit.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.lineEdit.setObjectName("lineEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 230, 431, 471))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(440, 230, 401, 31))
        self.label.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(460, 260, 361, 31))
        self.label_2.setStyleSheet("font: 14pt \".AppleSystemUIFont\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(460, 290, 361, 31))
        self.label_3.setStyleSheet("font: 14pt \".AppleSystemUIFont\";")
        self.label_3.setObjectName("label_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        CourseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CourseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 24))
        self.menubar.setObjectName("menubar")
        CourseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CourseWindow)
        self.statusbar.setObjectName("statusbar")
        CourseWindow.setStatusBar(self.statusbar)
        
        self.calendarWidget.selectionChanged.connect(self.get_date)
        # self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(CourseWindow)

    def get_date(self):
        dateSelected = str(self.calendarWidget.selectedDate().toString())[:3]
        day = "0"
        if dateSelected  == "Mon" or "周一":
            day = "1"
        elif dateSelected == "Tue" or "周二":
            day = "2"
        elif dateSelected == "Wed" or "周三":
            day = "3"
        elif dateSelected == "Thu" or "周四":
            day = "4"
        elif dateSelected == "Fri" or "周五":
            day = "5"
        elif dateSelected == "Sat" or "周六":
            day = "6"
        elif dateSelected == "Sun" or "周日":
            day = "7"

        print(day)
        conn = db.connect_db()
        course_info = db.get_course_data(conn, day)
        _translate = QtCore.QCoreApplication.translate
        CourseWindow.setWindowTitle(_translate("CourseWindow", "MainWindow"))
        self.lineEdit.setText(_translate("CourseWindow", "My Timetable"))
        if (len(course_info) > 0):
            self.label.setText(_translate("CourseWindow", f"{course_info[0][0]} - {course_info[0][1]}"))
            self.label_2.setText(_translate("CourseWindow", f"Time: {course_info[0][2]} - {course_info[0][3]}"))
            self.label_3.setText(_translate("CourseWindow", f"Course Venue: {course_info[0][4]}"))
            print(course_info)
    # def retranslateUi(self):
    #     # print(date)
    #     _translate = QtCore.QCoreApplication.translate
    #     CourseWindow.setWindowTitle(_translate("CourseWindow", "MainWindow"))
    #     self.lineEdit.setText(_translate("CourseWindow", "My Timetable"))
    #     self.label.setText(_translate("CourseWindow", "Comp3287 - Introduction to Database Management"))
    #     self.label_2.setText(_translate("CourseWindow", "Time: 11:00 - 12:00"))
    #     self.label_3.setText(_translate("CourseWindow", "Course Venue: CYM112"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CourseWindow = QtWidgets.QMainWindow()
    ui = Ui_CourseWindow()
    ui.setupUi(CourseWindow)
    CourseWindow.show()
    sys.exit(app.exec_())
