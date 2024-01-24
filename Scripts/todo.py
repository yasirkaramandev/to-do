# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard
import json
import datetime
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
        bugun_zaman = QtCore.QDateTime.currentDateTime()
        self.zaman_dateTimeEdit.setDateTime(bugun_zaman)
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
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(89, 258, 629, 657))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setMinimumSize(QtCore.QSize(670, 689))
        self.scrollArea.setMaximumSize(QtCore.QSize(624, 689))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 668, 687))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(QtCore.Qt.AlignTop)  # Frameleri üst tarafa hizala
        self.verticalLayout.setSpacing(0)  # Aralıkları sıfıra ayarla
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.todoList()
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
        self.delete_button.clicked.connect(self.deleteSelected)
    def closeDa(self):
        MainWindow.destroy(True,True)

    def addNewItem(self):
        if self.title_LineEdit.text() != "" or self.description_LineEdit.text() != "":
            # Data analyze
            title=self.title_LineEdit.text()
            description = self.description_LineEdit.text()
            date = self.zaman_dateTimeEdit.text()
            date_th = date.replace(".","/")
            date_time , date_hour = date_th.split(" ")

            # Data Set&Get

            with open("Data/data.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
            new_data = {"title": title, "description": description, "time": date}

            data.append(new_data)
            with open("Data/data.json","w",encoding="utf-8") as file:
                 json.dump(data,file,indent=4,ensure_ascii=False) # İndent 4 almamızın sebebi JSON dosyasında daha düzenli şekilde gözükmesini sağlamaktır.

            # Listeyi Güncelleme 
            self.todoList()
            # Kaydedince başa dönme

            self.title_LineEdit.setText("")
            self.description_LineEdit.setText("")
            self.zaman_dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        else: 
            QMessageBox = QtWidgets.QMessageBox()
            QMessageBox.warning(None,"Warning!","Please fill the fields.")
    def todoList(self):
        with open("Data/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        colors = ["#a6a6a6", "#737373"]
        self.color = 0

        for veri in data:
            if self.color == 0:
                self.color = 1
                useColor = colors[self.color]
            else:
                self.color = 0
                useColor = colors[self.color]

            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
            frame.setMinimumSize(QtCore.QSize(624, 88))
            frame.setMaximumSize(QtCore.QSize(624, 88))
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setStyleSheet(f"background-color:{useColor}")
            frame.setObjectName("frame")

            label_title = QtWidgets.QLabel(frame)
            label_title.setGeometry(QtCore.QRect(40, 10, 521, 31))
            label_title.setStyleSheet("""
                                    QLabel{
                                      color: #000;
                                      font-family: Arial;
                                      font-size: 22px;
                                      font-style: normal;
                                      font-weight: 700;
                                      line-height: normal;
                                      }
                                    """)
            label_title.setObjectName("label_4")
            title = veri["title"]
            label_title.setText(f"{title}")
            checkBox = QtWidgets.QCheckBox(frame)
            checkBox.setGeometry(QtCore.QRect(10, 30, 16, 21))
            checkBox.setText("")
            checkBox.setObjectName("checkBox")
            checkBox.stateChanged.connect(lambda x,labelTitle = label_title , check_box = checkBox: self.dataControl(labelTitle,check_box))
            label_desc = QtWidgets.QLabel(frame)
            label_desc.setGeometry(QtCore.QRect(40, 40, 491, 31))
            label_desc.setStyleSheet("QLabel{\n"
                                     "color: #000;\n"
                                     "font-family: Arial;\n"
                                     "font-size: 15px;\n"
                                     "font-style: normal;\n"
                                     "font-weight: 400;\n"
                                     "line-height: normal;\n"
                                     "}")
            label_desc.setObjectName("label_5")
            description = veri["description"]
            label_desc.setText(f"{description}")
            pushButton_3 = QtWidgets.QPushButton(frame)
            pushButton_3.setGeometry(QtCore.QRect(540, 30, 71, 41))
            pushButton_3.setStyleSheet("QPushButton{\n"
                                       "color: #FFF;\n"
                                       "text-align: center;\n"
                                       "font: 63 10pt \"Segoe UI\";\n"
                                       "font-weight: 700;\n"
                                       "background-color:rgb(2, 99, 255);\n"
                                       "}")
            pushButton_3.setObjectName("pushButton_3")
            pushButton_3.setText("More")
            self.verticalLayout.addWidget(frame)
    def dataControl(self,labelTitle,check_box):
        if check_box.isChecked():
            labelTitle.setStyleSheet("""
                                    QLabel{
                                      color: red;
                                      font-family: Arial;
                                      font-size: 22px;
                                      font-style: normal;
                                      font-weight: 700;
                                      line-height: normal;
                                      text-decoration: line-through;
                                      }
                                    """)
        else: 
            labelTitle.setStyleSheet("""
                                    QLabel{
                                      color: #000;
                                      font-family: Arial;
                                      font-size: 22px;
                                      font-style: normal;
                                      font-weight: 700;
                                      line-height: normal;
                                      text-decoration: line-through;
                                      }
                                    """)
    def deleteSelected(self):
        delete_indexes = []

        for i in range(self.verticalLayout.count()):
            frame = self.verticalLayout.itemAt(i).widget()
            checkbox = frame.findChild(QtWidgets.QCheckBox,"checkBox")
            if checkbox.isChecked():
                delete_indexes.append(i)

        with open("Data/data.json","r",encoding="utf-8") as file:
            data = json.load(file)

        for index in reversed(delete_indexes):
            del data[index]
        
        with open("Data/data.json","w",encoding="utf-8") as file:
            json.dump(data,file,ensure_ascii=False,indent=4)
        self.todoList()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    #text-decoration: line-through;
