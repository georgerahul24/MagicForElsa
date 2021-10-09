
def SecurityUI():
    import sys
    from PyQt5 import QtCore, QtWidgets
    from Magic import file_database,theme
    class Ui_Widget(object):
        def __init__(self):
            #Using reserverd keyword so tht in case user exits the login page it will show error
            self.username, self.password = f"users", f"1234"
            self.state=False


        def setupUi(self, Widget):
            Widget.setObjectName("Widget")
            Widget.resize(478, 310)
            self.stackedWidget = QtWidgets.QStackedWidget(Widget)
            self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 461, 291))
            self.stackedWidget.setObjectName("stackedWidget")
            self.loginPage = QtWidgets.QWidget()
            self.loginPage.setObjectName("loginPage")
            self.addNewUserButton = QtWidgets.QPushButton(self.loginPage)
            self.addNewUserButton.setGeometry(QtCore.QRect(250, 190, 131, 41))
            self.addNewUserButton.setObjectName("addNewUserButton")
            self.verifyUserButton = QtWidgets.QPushButton(self.loginPage)
            self.verifyUserButton.setGeometry(QtCore.QRect(120, 190, 111, 41))
            self.verifyUserButton.setObjectName("verifyUserButton")
            self.usernameLabel = QtWidgets.QLabel(self.loginPage)
            self.usernameLabel.setGeometry(QtCore.QRect(100, 40, 61, 51))
            self.usernameLabel.setObjectName("usernameLabel")
            self.usernameEntry = QtWidgets.QLineEdit(self.loginPage)
            self.usernameEntry.setGeometry(QtCore.QRect(171, 56, 211, 24))
            self.usernameEntry.setObjectName("usernameEntry")
            self.passwordLabel = QtWidgets.QLabel(self.loginPage)
            self.passwordLabel.setGeometry(QtCore.QRect(100, 110, 61, 41))
            self.passwordLabel.setObjectName("passwordLabel")
            self.passwordEntry = QtWidgets.QLineEdit(self.loginPage)
            self.passwordEntry.setGeometry(QtCore.QRect(171, 116, 211, 24))
            self.passwordEntry.setObjectName("passwordEntry")
            self.stackedWidget.addWidget(self.loginPage)
            self.AddUserPage = QtWidgets.QWidget()
            self.AddUserPage.setObjectName("AddUserPage")
            self.submitButton = QtWidgets.QPushButton(self.AddUserPage)
            self.submitButton.setGeometry(QtCore.QRect(240, 210, 101, 41))
            self.submitButton.setObjectName("submitButton")
            self.backButton = QtWidgets.QPushButton(self.AddUserPage)
            self.backButton.setGeometry(QtCore.QRect(120, 210, 101, 41))
            self.backButton.setObjectName("backButton")
            self.newUsernameLabel = QtWidgets.QLabel(self.AddUserPage)
            self.newUsernameLabel.setGeometry(QtCore.QRect(80, 50, 101, 51))
            self.newUsernameLabel.setObjectName("newUsernameLabel")
            self.newPasswordLabel = QtWidgets.QLabel(self.AddUserPage)
            self.newPasswordLabel.setGeometry(QtCore.QRect(80, 110, 101, 41))
            self.newPasswordLabel.setObjectName("newPasswordLabel")
            self.newUserNameEntry = QtWidgets.QLineEdit(self.AddUserPage)
            self.newUserNameEntry.setGeometry(QtCore.QRect(190, 70, 211, 24))
            self.newUserNameEntry.setObjectName("newUserNameEntry")
            self.newPasswordEntry = QtWidgets.QLineEdit(self.AddUserPage)
            self.newPasswordEntry.setGeometry(QtCore.QRect(190, 120, 211, 24))
            self.newPasswordEntry.setObjectName("newPasswordEntry")
            self.stackedWidget.addWidget(self.AddUserPage)

            self.retranslateUi(Widget)
            self.stackedWidget.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(Widget)
            self.initialiseWidgets()

        def initialiseWidgets(self):

            self.NotificationLabel = QtWidgets.QLabel(self.AddUserPage)
            self.verifyUserButton.clicked.connect(self.returnData)
            self.addNewUserButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
            self.submitButton.clicked.connect(self.addNewUser)
            self.backButton.clicked.connect(self.backButtonEvent)


        def returnData(self):
            self.state=True
            self.username, self.password = self.usernameEntry.text(), self.passwordEntry.text()
            Widget.close()
        def backButtonEvent(self):
            self.stackedWidget.setCurrentIndex(0)
            self.newPasswordEntry.clear()
            self.newUserNameEntry.clear()
            self.NotificationLabel.hide()
        def addNewUser(self):
            usrname = self.newUserNameEntry.text()
            passwd = self.newPasswordEntry.text()
            code = file_database.write_to_file(usrname, passwd)
            if code != 1:
                self.NotificationLabel.setStyleSheet('color:red')
                self.NotificationLabel.setGeometry(QtCore.QRect(60, 0, 500, 31))
                self.NotificationLabel.setText("Sorry!Please try another username.This username is reserved")
                self.NotificationLabel.show()
            else:
                self.NotificationLabel.setStyleSheet('color:green')
                self.NotificationLabel.setText('User Added Successfully')
                self.NotificationLabel.show()

        def retranslateUi(self, Widget):
            _translate = QtCore.QCoreApplication.translate
            Widget.setWindowTitle(_translate("Widget", "Elsa-Login Page"))
            self.addNewUserButton.setText(_translate("Widget", "Add New User"))
            self.verifyUserButton.setText(_translate("Widget", "Verify"))
            self.usernameLabel.setText(_translate("Widget", "Username:"))
            self.passwordLabel.setText(_translate("Widget", "Password:"))
            self.submitButton.setText(_translate("Widget", "Submit"))
            self.backButton.setText(_translate("Widget", "Back"))
            self.newUsernameLabel.setText(_translate("Widget", "New Username:"))
            self.newPasswordLabel.setText(_translate("Widget", "New Password:"))

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    app.exec_()
    if ui.state is False:
        sys.exit(1)


    return ui.username, ui.password
