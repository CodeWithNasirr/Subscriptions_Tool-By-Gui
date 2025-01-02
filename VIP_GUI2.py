import os
import json
import requests
import uuid
from PyQt5 import QtCore, QtGui, QtWidgets
import resource_rc
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(575, 340)
         # Remove minimize and close buttons
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-20, -10, 597, 322))
        self.stackedWidget.setObjectName("stackedWidget")

         # Set central widget
        self.setCentralWidget(self.centralwidget)
        
        self.init_license_page()

        self.check_existing_license()

    # Main Page Start Here
    def Main_Page(self):
        self.main_page_8 = QtWidgets.QWidget()
        self.main_page_8.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.main_page_8.setObjectName("main_page_8")
        #Header1 Start Here
        self.Header1 = QtWidgets.QFrame(self.main_page_8)
        self.Header1.setGeometry(QtCore.QRect(20, 10, 571, 50))
        self.Header1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Header1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header1.setObjectName("Header1")
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout(self.Header1)
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.Text_13 = QtWidgets.QLabel(self.Header1)
        self.Text_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Text_13.setFont(font)
        self.Text_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.Text_13.setAlignment(QtCore.Qt.AlignCenter)
        self.Text_13.setObjectName("Text_13")
        self.horizontalLayout_86.addWidget(self.Text_13, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.button_13 = QtWidgets.QFrame(self.Header1)
        self.button_13.setMaximumSize(QtCore.QSize(150, 16777215))
        self.button_13.setStyleSheet("")
        self.button_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_13.setObjectName("button_13")
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout(self.button_13)
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_87.setSpacing(6)
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.Close_13 = QtWidgets.QPushButton(self.button_13)
        self.Close_13.setMaximumSize(QtCore.QSize(46, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Close_13.setFont(font)
        self.Close_13.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border:0.5px solid red;")
        self.Close_13.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"ICONS/material-symbols--close-small-rounded.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close_13.setIcon(icon)
        self.Close_13.setIconSize(QtCore.QSize(30, 30))
        self.Close_13.setObjectName("Close_13")

        #Close Button
        self.Close_13.clicked.connect(self.close)
        self.horizontalLayout_87.addWidget(self.Close_13, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.horizontalLayout_86.addWidget(self.button_13, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        
        
        #Main Page Start Here
        self.Main = QtWidgets.QFrame(self.main_page_8)
        self.Main.setGeometry(QtCore.QRect(20, 110, 581, 162))
        self.Main.setMinimumSize(QtCore.QSize(0, 0))
        self.Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main.setObjectName("Main")
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout(self.Main)
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.frame_61 = QtWidgets.QFrame(self.Main)
        self.frame_61.setMinimumSize(QtCore.QSize(350, 160))
        self.frame_61.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_61.setStyleSheet("")
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_61)
        self.verticalLayout_38.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.frame_62 = QtWidgets.QFrame(self.frame_61)
        self.frame_62.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_62)
        self.verticalLayout_39.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.frame_63 = QtWidgets.QFrame(self.frame_62)
        self.frame_63.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_63.setMaximumSize(QtCore.QSize(150, 8))
        self.frame_63.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_63.setStyleSheet("background-color:transparent;\n"
"color: rgb(255, 255, 255);")
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setLineWidth(0)
        self.frame_63.setObjectName("frame_63")
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout(self.frame_63)
        self.horizontalLayout_89.setContentsMargins(10, 1, 1, 1)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.label_37 = QtWidgets.QLabel(self.frame_63)
        self.label_37.setMinimumSize(QtCore.QSize(0, 18))
        self.label_37.setMaximumSize(QtCore.QSize(129, 16))
        self.label_37.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_37.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_37.setWordWrap(False)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_89.addWidget(self.label_37)
        self.verticalLayout_39.addWidget(self.frame_63)
        self.label_38 = QtWidgets.QLabel(self.frame_62)
        self.label_38.setMinimumSize(QtCore.QSize(0, 0))
        self.label_38.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: white;\n"
"border: 1px dashed grey;\n"
"background-color: transparent;")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_39.addWidget(self.label_38)
        self.verticalLayout_38.addWidget(self.frame_62)
        self.horizontalLayout_88.addWidget(self.frame_61)
        self.frame_64 = QtWidgets.QFrame(self.Main)
        self.frame_64.setEnabled(False)
        self.frame_64.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_64.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.frame_64.setFont(font)
        self.frame_64.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame_64.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_64)
        self.verticalLayout_40.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.Register_succes_13 = QtWidgets.QLabel(self.frame_64)
        self.Register_succes_13.setMinimumSize(QtCore.QSize(0, 0))
        self.Register_succes_13.setMaximumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Register_succes_13.setFont(font)
        self.Register_succes_13.setLineWidth(1)
        self.Register_succes_13.setScaledContents(False)
        self.Register_succes_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Register_succes_13.setWordWrap(True)
        self.Register_succes_13.setObjectName("Register_succes_13")
        self.verticalLayout_40.addWidget(self.Register_succes_13)
        self.Welcome_text_13 = QtWidgets.QLabel(self.frame_64)
        self.Welcome_text_13.setMaximumSize(QtCore.QSize(85, 999))
        self.Welcome_text_13.show()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Welcome_text_13.setFont(font)
        self.Welcome_text_13.setWordWrap(True)
        self.Welcome_text_13.setObjectName("Welcome_text_13")
        self.verticalLayout_40.addWidget(self.Welcome_text_13)
        self.Thanks_Text_13 = QtWidgets.QLabel(self.frame_64)
        self.Thanks_Text_13.setMinimumSize(QtCore.QSize(0, 0))
        self.Thanks_Text_13.setMaximumSize(QtCore.QSize(85, 9999))
        self.Thanks_Text_13.hide()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(13)
        self.Thanks_Text_13.setFont(font)
        self.Thanks_Text_13.setWordWrap(True)
        self.Thanks_Text_13.setObjectName("Thanks_Text_13")
        self.verticalLayout_40.addWidget(self.Thanks_Text_13)
        self.Register_text_13 = QtWidgets.QLabel(self.frame_64)
        self.Register_text_13.setMinimumSize(QtCore.QSize(0, 0))
        self.Register_text_13.setMaximumSize(QtCore.QSize(85, 9999))
        self.Register_text_13.setSizeIncrement(QtCore.QSize(0, 0))
        self.Register_text_13.hide()
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.Register_text_13.setFont(font)
        self.Register_text_13.setMouseTracking(False)
        self.Register_text_13.setTabletTracking(False)
        self.Register_text_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.Register_text_13.setScaledContents(False)
        self.Register_text_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Register_text_13.setWordWrap(True)
        self.Register_text_13.setIndent(-1)
        self.Register_text_13.setObjectName("Register_text_13")
        self.verticalLayout_40.addWidget(self.Register_text_13, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_88.addWidget(self.frame_64, 0, QtCore.Qt.AlignRight)
        self.Header2 = QtWidgets.QFrame(self.main_page_8)
        self.Header2.setGeometry(QtCore.QRect(16, 70, 581, 40))
        self.Header2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Header2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header2.setObjectName("Header2")
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout(self.Header2)
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        self.frame_65 = QtWidgets.QFrame(self.Header2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame_65.setFont(font)
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout(self.frame_65)
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.label_39 = QtWidgets.QLabel(self.frame_65)
        self.label_39.setMinimumSize(QtCore.QSize(0, 0))
        self.label_39.setMaximumSize(QtCore.QSize(318, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_91.addWidget(self.label_39)
        self.horizontalLayout_90.addWidget(self.frame_65)
        self.Footer = QtWidgets.QFrame(self.main_page_8)
        self.Footer.setGeometry(QtCore.QRect(20, 280, 581, 41))
        self.Footer.setMinimumSize(QtCore.QSize(0, 0))
        self.Footer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Footer.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Footer.setFont(font)
        self.Footer.setStyleSheet("color: rgb(255, 255, 255);")
        self.Footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Footer.setLineWidth(0)
        self.Footer.setObjectName("Footer")
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout(self.Footer)
        self.horizontalLayout_85.setContentsMargins(0, 0, 160, 0)
        self.horizontalLayout_85.setSpacing(20)
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.pushButton_25 = QtWidgets.QPushButton(self.Footer)
        self.pushButton_25.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_25.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_25.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("background-color: rgb(88, 88, 88);")
        self.pushButton_25.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_85.addWidget(self.pushButton_25, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_26 = QtWidgets.QPushButton(self.Footer)
        self.pushButton_26.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_26.setStyleSheet("background-color: rgb(88, 88, 88);")
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_85.addWidget(self.pushButton_26, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget.addWidget(self.main_page_8)
        self.stackedWidget.setCurrentWidget(self.main_page_8)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    # Licence Page Start Here
    def init_license_page(self):
        self.Licence_Page=QtWidgets.QWidget()
        self.Licence_Page.setObjectName("Licence_Page")
        self.Licence_Main = QtWidgets.QFrame(self.Licence_Page)
        self.Licence_Main.setGeometry(QtCore.QRect(19, 9, 581, 311))
        self.Licence_Main.setStyleSheet("background-color: transparent;\n"
"color: rgb(209, 209, 209);")
        self.Licence_Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Licence_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Licence_Main.setObjectName("Licence_Main")
        self.label = QtWidgets.QLabel(self.Licence_Main)
        self.label.setGeometry(QtCore.QRect(10, 10, 561, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.Licence_Main)
        self.frame.setGeometry(QtCore.QRect(150, 70, 291, 211))
        self.frame.setStyleSheet("border:1px dashed grey")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid white")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.Active_Button = QtWidgets.QPushButton(self.frame)
        self.Active_Button.setGeometry(QtCore.QRect(90, 140, 101, 31))
        self.Active_Button.setStyleSheet("background-color: rgb(139, 139, 139);")
        self.Active_Button.setObjectName("Active_Button")
        #Acitve Calling here
        self.Active_Button.clicked.connect(self.check_license_key)
        self.Close_14 = QtWidgets.QPushButton(self.Licence_Main)
        self.Close_14.setGeometry(QtCore.QRect(535, 10, 31, 21))
        self.Close_14.setMaximumSize(QtCore.QSize(46, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Close_14.setFont(font)
        self.Close_14.setStyleSheet("""
    QPushButton {
        background-color: rgb(0, 0, 0);
        border: 0.5px solid red;
    }
    QPushButton:hover {
        background-color: white;
        border: 0.5px solid red;
    }
""")
        self.Close_14.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"ICONS/material-symbols--close-small-rounded.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close_14.setIcon(icon)
        #Close Button
        self.Close_14.clicked.connect(self.close)
        self.stackedWidget.addWidget(self.Licence_Page)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
 

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        try:
           self.Text_13.setText(_translate("MainWindow", "Latest Me Cleaner"))
           self.label_37.setText(_translate("MainWindow", "Drag&Drop Area"))
           self.label_38.setText(_translate("MainWindow", "Drag Here"))
           self.Register_succes_13.setText(_translate("MainWindow", "Registered Successfully For Activation Contact Xyzx 8093537813 "))
           self.Welcome_text_13.setText(_translate("MainWindow", "Welcome Nasir"))
           self.Thanks_Text_13.setText(_translate("MainWindow", "Thanks Nasir"))
           self.Register_text_13.setText(_translate("MainWindow", "Hello Click Registerd Button"))
           self.label_39.setText(_translate("MainWindow", "Only For IAS  2025 VIP Members"))
           self.pushButton_25.setText(_translate("MainWindow", "Build"))
           self.pushButton_26.setText(_translate("MainWindow", "CLEAR"))
        except AttributeError:
            pass  # Handle if the widgets are not yet initialized
        try:
           self.label.setText(_translate("MainWindow", "WELCOME TO THE VIP ISP ADVANCED TOOL"))
           self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Your Licence Key"))
           self.Active_Button.setText(_translate("MainWindow", "Activate"))
        except AttributeError:
             pass



    def check_license_key(self):
        license_key=self.lineEdit.text()#adsfghj
        device_id=self.get_device_id()
    
        try:
            # Connect to Django backend
            # url = "http://192.168.173.218:8000/api/validate-key/"
            url = "https://paid.pythonanywhere.com/api/validate-key/"
            response = requests.post(url, json={"key": license_key})

            if response.status_code == 200 or response.status_code == 202:
                self.save_license_key(license_key, device_id)
                print("Access Successfully")
                self.Main_Page()

            elif response.status_code == 403:
                print("Key already in use on another device ")

            elif response.status_code == 400:
                print("You Enterd Wrong Key!")
            else:
                print("You Enterd Wrong Key!")


        except requests.exceptions.RequestException as e:
            print("Error connecting to server:", e)

    def save_license_key(self,license_key,device_id):
        token_data = {"license_key": license_key,'Device_Id':device_id}
        with open("license_token.json", "w") as token_file:
            json.dump(token_data, token_file)

    def check_existing_license(self):
        if os.path.exists("license_token.json"):
            try:
                with open("license_token.json", "r") as token_file:
                    token_data = json.load(token_file)
                    license_key = token_data.get("license_key")
                    device_id=token_data.get("Device_Id")

                    # Validate the license key with django backend
                    url = "https://paid.pythonanywhere.com/api/validate-key/"
                    response = requests.post(url, json={"key": license_key,"device_id":device_id})

                    if response.status_code == 202:
                        print("Status 200")
                        self.Main_Page()

                    elif response.status_code == 403:
                        print("Key already in use on another device")

                    elif response.status_code == 400:
                        print("You Enterd Wrong Key!")

            except(json.JSONDecodeError,KeyError)as e:
                print("Error reading lincence token file",e)
        else:
            print('No Token Licence File Found')

    
    
    def get_device_id(self):
        return str(uuid.getnode())
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
