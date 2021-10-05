import json
import os
import pathlib
from functools import partial
from tkinter import Tk
from PyQt5 import QtCore, QtGui, QtWidgets

from Magic import theme, indexer, file_database


def folderchooser():
    from tkinter.filedialog import askdirectory
    folderpath = askdirectory()
    indexer.add_indexer_folders(path=folderpath)
    del folderpath


def filesInstaller():
    folderpath = os.getcwd() + "\\resources"
    folderpath = pathlib.Path(folderpath)
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    dummytpth = os.getcwd() + "\\resources\\ dummy.elsa"
    with open(dummytpth, "w") as f:
        f.write("Hey!The file you are looking is not found.Try again later")
    initpth = os.getcwd() + "\\resources\\ initial.elsa"
    with open(initpth, "w") as f:
        f.write(
            "black;purple;light green\n#The order is bg,font color,button colour\n#Please remember to use ';' to separate colours :D"
        )
    indexerpth = os.getcwd() + "\\resources\\ indexerpaths.elsa"
    with open(indexerpth, "w") as f:
        f.write("[]")
    userpth = os.getcwd() + "\\resources\\ users.elsa"
    with open(userpth, "w") as f:
        json.dump({"admin": "1234"}, f, indent=4)
    print("Added initial files")

def install_files():
    class Ui_MainWindow(object):
        def __init__(self):
            #Need to destroy Tk() else, when font etc is selected a Tk window will be shown.
            #This Tk window wont be closed thus causing problem with tkinter of Elsa when actually run
            self.tkin=Tk()
            #state == False means user forcefully closed the initial setup
            #state == True means setup completed successfully
            self.state = False

        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(800, 600)

            self.initialiseWidgets()
            self.SettingUpLinkages()

        def initialiseWidgets(self):
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
            self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 791, 581))
            self.stackedWidget.setObjectName("stackedWidget")
            self.StartPage = QtWidgets.QWidget()
            self.StartPage.setObjectName("StartPage")
            self.StartPageConitnueButton = QtWidgets.QPushButton(self.StartPage)
            self.StartPageConitnueButton.setGeometry(
                QtCore.QRect(630, 480, 131, 61))
            self.StartPageConitnueButton.setObjectName("StartPageConitnueButton")
            self.ElsaTitleLogo = QtWidgets.QLabel(self.StartPage)
            self.ElsaTitleLogo.setGeometry(QtCore.QRect(150, 60, 621, 191))
            font = QtGui.QFont()
            font.setFamily("Riviera")
            font.setPointSize(120)
            font.setBold(False)
            font.setWeight(50)
            self.ElsaTitleLogo.setFont(font)
            self.ElsaTitleLogo.setObjectName("ElsaTitleLogo")
            self.stackedWidget.addWidget(self.StartPage)
            self.LiscencePage = QtWidgets.QWidget()
            self.LiscencePage.setObjectName("LiscencePage")
            self.LicenceLabel = QtWidgets.QLabel(self.LiscencePage)
            self.LicenceLabel.setGeometry(QtCore.QRect(-10, -90, 771, 581))
            self.LicenceLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.LicenceLabel.setObjectName("LicenceLabel")
            self.AgreeRadioButton = QtWidgets.QRadioButton(self.LiscencePage)
            self.AgreeRadioButton.setGeometry(QtCore.QRect(50, 420, 131, 41))
            self.AgreeRadioButton.setObjectName("AgreeRadioButton")
            self.DisAgreeRadioButton = QtWidgets.QRadioButton(self.LiscencePage)
            self.DisAgreeRadioButton.setGeometry(QtCore.QRect(50, 450, 131, 41))
            self.DisAgreeRadioButton.setObjectName("DisAgreeRadioButton")
            self.LicenceContinueButton = QtWidgets.QPushButton(self.LiscencePage)
            self.LicenceContinueButton.setGeometry(QtCore.QRect(630, 510, 101, 51))
            self.LicenceContinueButton.setObjectName("LicenceContinueButton")
            self.stackedWidget.addWidget(self.LiscencePage)
            self.AddUserPage = QtWidgets.QWidget()
            self.AddUserPage.setObjectName("AddUserPage")
            self.EnterUsernameTextBox = QtWidgets.QLineEdit(self.AddUserPage)
            self.EnterUsernameTextBox.setGeometry(QtCore.QRect(330, 150, 281, 31))
            self.EnterUsernameTextBox.setObjectName("EnterUsernameTextBox")
            self.EnterPasswordTextBox = QtWidgets.QLineEdit(self.AddUserPage)
            self.EnterPasswordTextBox.setGeometry(QtCore.QRect(330, 210, 281, 31))
            self.EnterPasswordTextBox.setObjectName("EnterPasswordTextBox")
            self.EnterUserNameLabel = QtWidgets.QLabel(self.AddUserPage)
            self.EnterUserNameLabel.setGeometry(QtCore.QRect(160, 150, 151, 31))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.EnterUserNameLabel.setFont(font)
            self.EnterUserNameLabel.setObjectName("EnterUserNameLabel")
            self.EnterPasswordLabel = QtWidgets.QLabel(self.AddUserPage)
            self.EnterPasswordLabel.setGeometry(QtCore.QRect(160, 210, 151, 31))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.EnterPasswordLabel.setFont(font)
            self.EnterPasswordLabel.setObjectName("EnterPasswordLabel")
            self.AddNewUserTitleLabel = QtWidgets.QLabel(self.AddUserPage)
            self.AddNewUserTitleLabel.setGeometry(QtCore.QRect(110, 50, 521, 61))
            font = QtGui.QFont()
            font.setPointSize(28)
            font.setBold(True)
            font.setWeight(75)
            self.AddNewUserTitleLabel.setFont(font)
            self.AddNewUserTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.AddNewUserTitleLabel.setObjectName("AddNewUserTitleLabel")
            self.AddUserContinueButton = QtWidgets.QPushButton(self.AddUserPage)
            self.AddUserContinueButton.setGeometry(QtCore.QRect(620, 500, 121, 41))
            self.AddUserContinueButton.setObjectName("AddUserContinueButton")
            self.stackedWidget.addWidget(self.AddUserPage)
            self.OthersPage = QtWidgets.QWidget()
            self.OthersPage.setObjectName("OthersPage")
            self.ButtonColorButton = QtWidgets.QPushButton(self.OthersPage)
            self.ButtonColorButton.setGeometry(QtCore.QRect(290, 230, 181, 61))
            self.ButtonColorButton.setObjectName("ButtonColorButton")
            self.TextColorButton = QtWidgets.QPushButton(self.OthersPage)
            self.TextColorButton.setGeometry(QtCore.QRect(290, 90, 181, 61))
            self.TextColorButton.setObjectName("TextColorButton")
            self.BackGroundColorButton = QtWidgets.QPushButton(self.OthersPage)
            self.BackGroundColorButton.setGeometry(QtCore.QRect(290, 160, 181, 61))
            self.BackGroundColorButton.setObjectName("BackGroundColorButton")
            self.NewThemeLabel = QtWidgets.QLabel(self.OthersPage)
            self.NewThemeLabel.setGeometry(QtCore.QRect(210, 10, 371, 91))
            font = QtGui.QFont()
            font.setPointSize(18)
            font.setBold(True)
            font.setWeight(75)
            self.NewThemeLabel.setFont(font)
            self.NewThemeLabel.setObjectName("NewThemeLabel")
            self.AddnFolderLabel = QtWidgets.QLabel(self.OthersPage)
            self.AddnFolderLabel.setGeometry(QtCore.QRect(130, 300, 521, 91))
            font = QtGui.QFont()
            font.setPointSize(18)
            font.setBold(True)
            font.setWeight(75)
            self.AddnFolderLabel.setFont(font)
            self.AddnFolderLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.AddnFolderLabel.setObjectName("AddnFolderLabel")
            self.AddFolderButton = QtWidgets.QPushButton(self.OthersPage)
            self.AddFolderButton.setGeometry(QtCore.QRect(300, 380, 181, 61))
            self.AddFolderButton.setObjectName("AddFolderButton")
            self.ContinueOtherButton = QtWidgets.QPushButton(self.OthersPage)
            self.ContinueOtherButton.setGeometry(QtCore.QRect(600, 510, 181, 61))
            self.ContinueOtherButton.setObjectName("ContinueOtherButton")
            self.stackedWidget.addWidget(self.OthersPage)
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def SettingUpLinkages(self):
            # ...disabling Licnece Button...
            self.LicenceContinueButton.setDisabled(True)
            # ....continue Buttons.........
            self.StartPageConitnueButton.clicked.connect(
                partial(self.stackedWidget.setCurrentIndex, 1))
            self.LicenceContinueButton.clicked.connect(self.LicenseAcceptEvent)
            self.AddUserContinueButton.clicked.connect(self.adduserevent)
            self.ContinueOtherButton.clicked.connect(self.finishInitialSetup)
            # ....Radio Buttons......
            self.AgreeRadioButton.clicked.connect(
                partial(self.LicenceContinueButton.setDisabled, False))
            self.DisAgreeRadioButton.clicked.connect(
                partial(self.LicenceContinueButton.setDisabled, True))

            # .....Theme Buttons.....
            self.BackGroundColorButton.clicked.connect(theme.new_background_colour)
            self.TextColorButton.clicked.connect(theme.new_font_colour)
            self.ButtonColorButton.clicked.connect(theme.new_button_colour)
            # ....Indexer Button.......
            self.AddFolderButton.clicked.connect(folderchooser)

        def LicenseAcceptEvent(self):
            self.stackedWidget.setCurrentIndex(2)
            filesInstaller()

        def finishInitialSetup(self):
            #Setting state=True so that it indicates that setup was successful and not closed by the user
            self.state = True
            #deleteing tkin so that the background window
            #of askdirectory() and colorchooser() are destroyed properly
            self.tkin.destroy()
            MainWindow.close()

        def adduserevent(self):
            usrname = self.EnterUsernameTextBox.text()
            passwd = self.EnterPasswordTextBox.text()
            code = file_database.write_to_file(usrname, passwd)
            if code == 1:
                self.stackedWidget.setCurrentIndex(3)
            else:
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)

                self.ErrorLabel = QtWidgets.QLabel(self.AddUserPage)
                self.ErrorLabel.setFont(font)
                self.ErrorLabel.setGeometry(QtCore.QRect(160, 450, 500, 31))
                self.ErrorLabel.setText(
                    "Sorry!Please try another username.This username is reserved")
                self.ErrorLabel.show()

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(
                _translate("MainWindow", "Elsa-Initial Setup"))
            self.StartPageConitnueButton.setText(
                _translate("MainWindow", "Continue"))
            self.ElsaTitleLogo.setText(_translate("MainWindow", "Elsa"))
            self.LicenceLabel.setText(
                _translate(
                    "MainWindow", "MIT License\n"
                    "\n"
                    "Copyright (c) 2021 George Rahul\n"
                    "\n"
                    "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
                    "of this software and associated documentation files (the \"Software\"), to deal\n"
                    "in the Software without restriction, including without limitation the rights\n"
                    "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
                    "copies of the Software, and to permit persons to whom the Software is\n"
                    "furnished to do so, subject to the following conditions:\n"
                    "\n"
                    "The above copyright notice and this permission notice shall be included in all\n"
                    "copies or substantial portions of the Software.\n"
                    "\n"
                    "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
                    "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
                    "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
                    "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
                    "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
                    "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n"
                    "SOFTWARE.\n"
                    ""))
            self.AgreeRadioButton.setText(_translate("MainWindow", "I Agree"))
            self.DisAgreeRadioButton.setText(_translate("MainWindow",
                                                        "I Disagree"))
            self.LicenceContinueButton.setText(_translate("MainWindow",
                                                          "Continue"))
            self.EnterUserNameLabel.setText(
                _translate("MainWindow", "Enter Username:"))
            self.EnterPasswordLabel.setText(
                _translate("MainWindow", "Enter Password:"))
            self.AddNewUserTitleLabel.setText(
                _translate("MainWindow", "Add New User"))
            self.AddUserContinueButton.setText(_translate("MainWindow",
                                                          "Continue"))
            self.ButtonColorButton.setText(_translate("MainWindow",
                                                      "Button Color"))
            self.TextColorButton.setText(_translate("MainWindow", "Text Color"))
            self.BackGroundColorButton.setText(
                _translate("MainWindow", "Background Color"))
            self.NewThemeLabel.setText(
                _translate("MainWindow", "Select  A New Theme"))
            self.AddnFolderLabel.setText(
                _translate("MainWindow", "Add Additional Folders To Index"))
            self.AddFolderButton.setText(_translate("MainWindow", "Add Folder"))
            self.ContinueOtherButton.setText(_translate("MainWindow", "Finish"))


    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)



    MainWindow.show()
    app.exec_()
    if ui.state is False:
        sys.exit(1)
