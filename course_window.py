# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'course_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import database_model as db
from email_notification import send_email, Ui_EmailWindow
import datetime

class Ui_ClassWindow(object):
    def setupUi(self, ClassWindow):
        ClassWindow.setObjectName("CourseWindow")
        ClassWindow.resize(772, 926)
        self.centralwidget = QtWidgets.QWidget(ClassWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1141, 881))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1139, 879))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1141, 881))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 461, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("assets/woodle_logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 170, 541, 51))
        self.lineEdit.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget, clicked = lambda:self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(570, 170, 161, 41))
        self.pushButton.setStyleSheet("background-color: rgb(210, 210, 210);\n"
"border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 220, 771, 41))
        self.label.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"background-color: rgb(240, 240, 240);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 260, 131, 41))
        self.label_2.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 300, 131, 41))
        self.label_3.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font-weight: bold;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(0, 380, 131, 41))
        self.label_5.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(0, 340, 141, 41))
        self.label_6.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(0, 420, 131, 41))
        self.label_7.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"font-weight: bold;")
        self.label_7.setObjectName("label_7")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.widget)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 220, 771, 661))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 769, 659))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setGeometry(QtCore.QRect(160, 40, 611, 41))
        self.label_8.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"")
        self.label_8.setObjectName("label_8")
        ## hyperlink
        
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setGeometry(QtCore.QRect(160, 200, 611, 41))
        self.label_12.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"")
        self.label_12.setObjectName("label_12")
        ## hyperlink
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setGeometry(QtCore.QRect(160, 160, 611, 41))
        self.label_11.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setGeometry(QtCore.QRect(160, 120, 611, 41))
        self.label_10.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setGeometry(QtCore.QRect(160, 80, 611, 41))
        self.label_9.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"")
        self.label_9.setObjectName("label_9")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 450, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea_2.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.line.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        ClassWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ClassWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 24))
        self.menubar.setObjectName("menubar")
        ClassWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ClassWindow)
        self.statusbar.setObjectName("statusbar")
        ClassWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ClassWindow)
        QtCore.QMetaObject.connectSlotsByName(ClassWindow)

    def retranslateUi(self, ClassWindow):
        time = "11:00" ## Todo: function needed to get the current time(import time??)
        weekday = "2"  ## Todo: function needed to get weekday now
        conn = db.connect_db()
        user_id, _, _ = db.get_name_time(conn)
        course_info = db.get_course_in_an_hour(conn, user_id, time, weekday)
        _translate = QtCore.QCoreApplication.translate
        ClassWindow.setWindowTitle(_translate("ClassWindow", "MainWindow"))
        self.lineEdit.setText(_translate("ClassWindow", "My Courses"))
        self.pushButton.setText(_translate("ClassWindow", "Send information to mail"))
        self.label.setText(_translate("ClassWindow", "Course information - "+course_info[0][1]+": "+course_info[0][0]))
        self.label_2.setText(_translate("ClassWindow", " Course Teacher:"))
        self.label_3.setText(_translate("ClassWindow", " Course Address:"))
        self.label_5.setText(_translate("ClassWindow", " Zoom Link:"))
        self.label_6.setText(_translate("ClassWindow", " Teacher message:"))
        self.label_7.setText(_translate("ClassWindow", " Lecture Notes:"))
        self.label_8.setText(_translate("ClassWindow", course_info[0][6]))
        self.label_12.setText(_translate("ClassWindow", course_info[0][5])) ## To do: material link
        self.label_11.setText(_translate("ClassWindow", course_info[0][4])) ## To do: zoom link
        self.label_10.setText(_translate("ClassWindow", course_info[0][3]))
        self.label_9.setText(_translate("ClassWindow", course_info[0][2]))
        
    def openWindow(self):
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.strftime("%H:%M")
        current_day = current_date_time.strftime("%A")[:3]
        if current_day  == "Mon":
            current_day = "1"
        elif current_day == "Tue":
            current_day = "2"
        elif current_day == "Wed":
            current_day = "3"
        elif current_day == "Thu":
            current_day = "4"
        elif current_day == "Fri":
            current_day = "5"
        elif current_day == "Sat":
            current_day = "6"
        elif current_day == "Sun":
            current_day = "7"
        else:
            current_day = "0"
            
        conn = db.connect_db()
        user_id, _, _ = db.get_name_time(conn)
        course_info = db.get_course_in_an_hour(conn, user_id, current_time, current_day)
        user_email = db.get_user_email(conn, user_id)
        message = send_email(user_email, course_info)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EmailWindow()
        self.ui.setupUi(self.window, message)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClassWindow = QtWidgets.QMainWindow()
    ui = Ui_ClassWindow()
    ui.setupUi(ClassWindow)
    ClassWindow.show()
    sys.exit(app.exec_())
