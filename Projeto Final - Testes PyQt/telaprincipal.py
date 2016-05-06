# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaprincipal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pedircarona

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
        self.titulo.setGeometry(QtCore.QRect(140, 70, 531, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(28)
        self.titulo.setFont(font)
        self.titulo.setObjectName(_fromUtf8("titulo"))

        #Botão de agendar a carona
        self.agendar = QtGui.QPushButton(self.centralwidget)
        self.agendar.setGeometry(QtCore.QRect(260, 340, 300, 50))
        self.agendar.setObjectName(_fromUtf8("agendar"))

        #Botão de pedir a carona
        self.pedir = QtGui.QPushButton(self.centralwidget)
        self.pedir.setGeometry(QtCore.QRect(260, 250, 300, 50))
        self.pedir.setObjectName(_fromUtf8("pedir"))
        self.pedir.clicked.connect(self.abrirpedir)

        #Botão para alterar o perfil
        self.perfil = QtGui.QPushButton(self.centralwidget)
        self.perfil.setGeometry(QtCore.QRect(260, 430, 300, 50))
        self.perfil.setObjectName(_fromUtf8("perfil"))

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.statuslabel.setText(_translate("MainWindow", "Status da carona:", None))
        self.titulo.setText(_translate("MainWindow", "Olá, (usuario). O que deseja fazer?", None))
        self.agendar.setText(_translate("MainWindow", "Agendar carona", None))
        self.pedir.setText(_translate("MainWindow", "Pedir carona", None))
        self.perfil.setText(_translate("MainWindow", "Alterar perfil", None))
        self.statusdacarona.setText(_translate("MainWindow", "Inativo/Pendente/Ativo", None))

    def abrirpedir(self):
        self.MainWindow = pedircarona.Ui_MainWindow
        telapedir = QtGui.QMainWindow()
        ui = pedircarona.Ui_MainWindow()
        ui.setupUi(telapedir)
        telapedir.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

