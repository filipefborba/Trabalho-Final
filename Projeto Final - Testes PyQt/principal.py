# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaprincipal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import caronas, pedircarona, agendarcarona, removercarona, perfil

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Frame da janela
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Cor da janela (ativa,inativa,desativada)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)

        #Label do status da carona
        self.statuslabel = QtGui.QLabel(self.centralwidget)
        self.statuslabel.setGeometry(QtCore.QRect(80, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.statuslabel.setFont(font)
        self.statuslabel.setObjectName(_fromUtf8("statuslabel"))

        #Título de boas-vindas
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(120, 70, 571, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(28)
        self.titulo.setFont(font)
        self.titulo.setObjectName(_fromUtf8("titulo"))

        #Botão de agendar a carona
        self.agendar = QtGui.QPushButton(self.centralwidget)
        self.agendar.setGeometry(QtCore.QRect(260, 340, 300, 50))
        self.agendar.setObjectName(_fromUtf8("agendar"))
        self.agendar.clicked.connect(self.abriragendar)


        #Botão de pedir a carona
        self.pedir = QtGui.QPushButton(self.centralwidget)
        self.pedir.setGeometry(QtCore.QRect(260, 250, 300, 50))
        self.pedir.setObjectName(_fromUtf8("pedir"))
        self.pedir.clicked.connect(self.abrirpedir)

        #Botão para alterar o perfil
        self.perfil = QtGui.QPushButton(self.centralwidget)
        self.perfil.setGeometry(QtCore.QRect(260, 500, 300, 50))
        self.perfil.setObjectName(_fromUtf8("perfil"))
        self.perfil.clicked.connect(self.abrirperfil)

        #Botão para remover a carona
        self.remover = QtGui.QPushButton(self.centralwidget)
        self.remover.setGeometry(QtCore.QRect(260, 420, 300, 50))
        self.remover.setObjectName(_fromUtf8("remover"))
        self.remover.clicked.connect(self.abrirremover)

        #Botão para fazer logout
        self.logout = QtGui.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(0, 530, 101, 31))
        self.logout.setObjectName(_fromUtf8("logout"))
        self.logout.clicked.connect(self.abrircaronas)

        #Label representativa do status ##SERÁ MUDADO##
        self.statusdacarona = QtGui.QLabel(self.centralwidget)
        self.statusdacarona.setGeometry(QtCore.QRect(220, 180, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.statusdacarona.setFont(font)
        self.statusdacarona.setObjectName(_fromUtf8("statusdacarona"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Função que define os textos dentro dos botões e da janela
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Caronas Insper", None))
        self.statuslabel.setText(_translate("MainWindow", "Status da carona:", None))
        self.titulo.setText(_translate("MainWindow", "Seja bem-vindo! O que deseja fazer?", None))
        self.agendar.setText(_translate("MainWindow", "Agendar carona", None))
        self.pedir.setText(_translate("MainWindow", "Pedir carona", None))
        self.perfil.setText(_translate("MainWindow", "Alterar perfil", None))
        self.statusdacarona.setText(_translate("MainWindow", "Inativo/Pendente/Ativo", None))
        self.remover.setText(_translate("MainWindow", "Remover carona pedida/agendada", None))
        self.logout.setText(_translate("MainWindow", "Log Out", None))


    def abrirpedir(self):
        self.MainWindow = pedircarona.Ui_MainWindow
        telapedir = QtGui.QMainWindow()
        ui = pedircarona.Ui_MainWindow()
        ui.setupUi(telapedir)
        telapedir.show()
        sys.exit(app.exec_())

    def abriragendar(self):
        self.MainWindow = agendarcarona.Ui_MainWindow
        tela_agendar = QtGui.QMainWindow()
        ui = agendarcarona.Ui_MainWindow()
        ui.setupUi(tela_agendar)
        tela_agendar.show()
        sys.exit(app.exec_())

    def abrirremover(self):
        self.MainWindow = removercarona.Ui_MainWindow
        tela_remover = QtGui.QMainWindow()
        ui = removercarona.Ui_MainWindow()
        ui.setupUi(tela_remover)
        tela_remover.show()
        sys.exit(app.exec_())


    def abrirperfil(self):
        self.MainWindow = perfil.Ui_MainWindow
        tela_perfil = QtGui.QMainWindow()
        ui = perfil.Ui_MainWindow()
        ui.setupUi(tela_perfil)
        tela_perfil.show()
        sys.exit(app.exec_())


    def abrircaronas(self):
        self.MainWindow = caronas.Ui_MainWindow
        tela_caronas = QtGui.QMainWindow()
        ui = caronas.Ui_MainWindow()
        ui.setupUi(tela_caronas)
        tela_caronas.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

