# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard
import json
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1088)
        MainWindow.setStyleSheet("background-image: url(Assets/main.png);")
        MainWindow.showFullScreen()
        keyboard.add_hotkey('esc',self.closeDa)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.widget.setStyleSheet("background-image: url();")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(1240, 360, 111, 71))
        self.label.setStyleSheet("QLabel{\n"
"color: #FFF;\n"
"font-family: Arial;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.label.setObjectName("label")
        self.title_LineEdit = QtWidgets.QLineEdit(self.widget)
        self.title_LineEdit.setGeometry(QtCore.QRect(1240, 420, 580, 50))
        self.title_LineEdit.setStyleSheet("\n"
"QLineEdit{\n"
"background-color: rgb(189, 186, 186);\n"
"border:none;\n"
"color: #fff;\n"
"font-family: Arial;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding-left:10px;\n"
"}")
        self.title_LineEdit.setObjectName("title_LineEdit")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(1240, 470, 131, 51))
        self.label_2.setStyleSheet("QLabel{\n"
"color: #FFF;\n"
"font-family: Arial;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.description_LineEdit = QtWidgets.QLineEdit(self.widget)
        self.description_LineEdit.setGeometry(QtCore.QRect(1240, 520, 580, 50))
        self.description_LineEdit.setStyleSheet("\n"
"QLineEdit{\n"
"background-color: rgb(189, 186, 186);\n"
"border:none;\n"
"color: #fff;\n"
"font-family: Arial;\n"
"font-size: 26px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"padding-left:10px;\n"
"}")
        self.description_LineEdit.setObjectName("description_LineEdit")
        self.zaman_dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.zaman_dateTimeEdit.setGeometry(QtCore.QRect(1240, 610, 291, 51))
        self.zaman_dateTimeEdit.setStyleSheet("color: #5E5E5E;\n"
"font-family: Arial;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.zaman_dateTimeEdit.setObjectName("zaman_dateTimeEdit")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(1240, 567, 131, 51))
        self.label_3.setStyleSheet("QLabel{\n"
"color: #FFF;\n"
"font-family: Arial;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.add_button = QtWidgets.QPushButton(self.widget)
        self.add_button.setGeometry(QtCore.QRect(1240, 680, 580, 50))
        self.add_button.setStyleSheet("QPushButton{\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: Segoe UI;\n"
"font-size: 20px;\n"
"font-style: SemiBold;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"    background-color:#0019FF;;\n"
"}")
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.addNewItem)
        self.delete_button = QtWidgets.QPushButton(self.widget)
        self.delete_button.setGeometry(QtCore.QRect(590, 200, 131, 50))
        self.delete_button.setStyleSheet("QPushButton{\n"
"color: #FFF;\n"
"text-align: center;\n"
"font: 63 10pt \"Segoe UI\";\n"
"font-weight: 700;\n"
"background-color:#F11111;\n"
"}")
        self.delete_button.setObjectName("delete_button")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 260, 631, 661))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame.setMinimumSize(QtCore.QSize(624, 88))
        self.frame.setMaximumSize(QtCore.QSize(624, 88))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 521, 31))
        self.label_4.setStyleSheet("QLabel{\n"
"color: #000;\n"
"font-family: Arial;\n"
"font-size: 22px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 16, 21))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 491, 31))
        self.label_5.setStyleSheet("QLabel{\n"
"color: #000;\n"
"font-family: Arial;\n"
"font-size: 15px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 30, 71, 41))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color: #FFF;\n"
"text-align: center;\n"
"font: 63 10pt \"Segoe UI\";\n"
"font-weight: 700;\n"
"background-color:rgb(2, 99, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Title (*)"))
        self.title_LineEdit.setPlaceholderText(_translate("MainWindow", "Title..."))
        self.label_2.setText(_translate("MainWindow", "Description (*)"))
        self.description_LineEdit.setPlaceholderText(_translate("MainWindow", "Description..."))
        self.label_3.setText(_translate("MainWindow", "Date"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.label_4.setText(_translate("MainWindow", "Title"))
        self.label_5.setText(_translate("MainWindow", "Description"))
        self.pushButton_3.setText(_translate("MainWindow", "More"))
    def closeDa(self):
        MainWindow.destroy(True,True)


    def addNewItem(self):
        # Data analyze
        title=self.title_LineEdit.text()
        description = self.description_LineEdit.text()
        date = self.zaman_dateTimeEdit.text()
        date_th = date.replace(".","/")
        date_time , date_hour = date_th.split(" ")
        print("title: ",title," description: ",description, " tarih: ",date_time ," Saat Dakika: ", type(date))
        # Data Set&Get
        with open("Data/data.json","r",encoding="utf-8") as file:
                data = json.load(file)
        print("old: ",data)
        new_data = {"title":title,"description": description, "time":data}
        data.append(new_data)
        print("new: ",data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
