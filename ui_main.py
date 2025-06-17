# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_1.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(265, 265, 265);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_outro = QPushButton(self.frame)
        self.btn_outro.setObjectName(u"btn_outro")

        self.horizontalLayout.addWidget(self.btn_outro)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_3 = QVBoxLayout(self.pg_table)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.horizontalLayout_2 = QHBoxLayout(self.tables)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_file = QLineEdit(self.frame_2)
        self.txt_file.setObjectName(u"txt_file")

        self.horizontalLayout_3.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.frame_2)
        self.btn_open.setObjectName(u"btn_open")

        self.horizontalLayout_3.addWidget(self.btn_open)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.tw_estoque = QTreeWidget(self.frame_2)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_7.addWidget(self.tw_estoque)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tw_saida = QTreeWidget(self.frame_2)
        self.tw_saida.setObjectName(u"tw_saida")

        self.verticalLayout_5.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_importar = QPushButton(self.frame_3)
        self.btn_importar.setObjectName(u"btn_importar")

        self.verticalLayout.addWidget(self.btn_importar)

        self.btn_gerar = QPushButton(self.frame_3)
        self.btn_gerar.setObjectName(u"btn_gerar")

        self.verticalLayout.addWidget(self.btn_gerar)

        self.btn_estorno = QPushButton(self.frame_3)
        self.btn_estorno.setObjectName(u"btn_estorno")

        self.verticalLayout.addWidget(self.btn_estorno)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_4 = QVBoxLayout(self.pg_home)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.pg_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.pg_home)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.btn_pg_cadastro = QPushButton(self.pg_home)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")

        self.horizontalLayout_5.addWidget(self.btn_pg_cadastro)

        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_10 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")
        font = QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_12)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")

        self.horizontalLayout_6.addWidget(self.txt_nome)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")

        self.horizontalLayout_7.addWidget(self.txt_usuario)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_8.addWidget(self.txt_senha)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_9.addWidget(self.txt_senha_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")

        self.horizontalLayout_10.addWidget(self.cb_perfil)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")

        self.horizontalLayout_11.addWidget(self.btn_cadastrar)

        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.formLayout = QFormLayout(self.pg_contato)
        self.formLayout.setObjectName(u"formLayout")
        self.label_15 = QLabel(self.pg_contato)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_15)

        self.Pages.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.formLayout_2 = QFormLayout(self.pg_sobre)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_16 = QLabel(self.pg_sobre)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_16)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.Pages.raise_()
        self.frame.raise_()

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABLE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_outro.setText(QCoreApplication.translate("MainWindow", u"OUTRO", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Especie", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"UN", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Cod item", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data de Sa\u00edda", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar sa\u00edda", None))
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700; color:#00007f;\">SISTEMA</span></p><p align=\"center\"><span style=\" font-size:48pt; font-weight:700; color:#00007f;\">DE</span></p><p align=\"center\"><span style=\" font-size:48pt; font-weight:700; color:#00007f;\">GERENCIAMENTO</span><span style=\" font-size:48pt; font-weight:700; color:#ffffff;\">.</span></p></body></html>", None))
        self.label_5.setText("")
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_4.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tela de Cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USU\u00c1RIO", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_13.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"                                                Tela de contatos", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
    # retranslateUi

