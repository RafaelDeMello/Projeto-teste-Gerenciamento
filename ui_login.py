# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(588, 584)
        Login.setStyleSheet(u"background-color: rgb(0. 255, 255);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 0, 501, 581))
        self.frame.setStyleSheet(u"background-color :rgb(0, 74, 112);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 0, 181, 111))
        self.label.setPixmap(QPixmap(u"_imgs/icon_title.png"))
        self.label.setScaledContents(True)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 200, 231, 261))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_user = QLineEdit(self.layoutWidget)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setCursor(QCursor(Qt.CursorShape.SizeAllCursor))
        self.txt_user.setStyleSheet(u"")
        self.txt_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.txt_user)

        self.txt_password = QLineEdit(self.layoutWidget)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.txt_password)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.btn_login = QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"\n"
"      background-color: rgb(0, 0, 0);\n"
"      color: rgb(255, 255, 255);\n"
"      border-radiu: 15px;\n"
"      transition: 0.5s;\n"
"\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_login)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label.setText("")
        self.txt_user.setText("")
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi

