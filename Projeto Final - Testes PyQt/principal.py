# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaprincipal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import caronas, pedircarona, agendarcarona, removercarona, perfil, login
from firebase import firebase

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
    def setupUi(self, MainWindow, usuarios, nome, tel, email):
        self.usuarios = usuarios
        self.nome_completo = nome
        self.telefone = tel
        self.email = email

        #Frame da janela
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800,600)
        MainWindow.setWindowIcon(QtGui.QIcon("Fotos/carro.jpg"))
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
        self.agendar.setGeometry(QtCore.QRect(230, 270, 321, 50))
        self.agendar.setObjectName(_fromUtf8("agendar"))
        self.agendar.clicked.connect(self.abriragendar)


        #Botão de pedir a carona
        self.pedir = QtGui.QPushButton(self.centralwidget)
        self.pedir.setGeometry(QtCore.QRect(230, 190, 321, 50))
        self.pedir.setObjectName(_fromUtf8("pedir"))
        self.pedir.clicked.connect(self.abrirpedir)

        #Botão para alterar o perfil
        self.perfil = QtGui.QPushButton(self.centralwidget)
        self.perfil.setGeometry(QtCore.QRect(230, 430, 321, 50))
        self.perfil.setObjectName(_fromUtf8("perfil"))
        self.perfil.clicked.connect(self.abrirperfil)

        #Botão para remover o pedido de carona
        self.remover = QtGui.QPushButton(self.centralwidget)
        self.remover.setGeometry(QtCore.QRect(230, 350, 161, 50))
        self.remover.setObjectName(_fromUtf8("remover"))
        self.remover.clicked.connect(self.removerpedido)

        #Botão para remover a oferta de carona
        self.remover2 = QtGui.QPushButton(self.centralwidget)
        self.remover2.setGeometry(QtCore.QRect(390, 350, 161, 50))
        self.remover2.setObjectName(_fromUtf8("remover"))
        self.remover2.clicked.connect(self.removeroferta)

        #Botão para fazer logout
        self.logout = QtGui.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(0, 530, 101, 31))
        self.logout.setObjectName(_fromUtf8("logout"))
        self.logout.clicked.connect(self.abrircaronas)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Função que define os textos dentro dos botões e da janela
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Caronas Insper", None))
        self.titulo.setText(_translate("MainWindow", "Seja bem-vindo! O que deseja fazer?", None))
        self.agendar.setText(_translate("MainWindow", "Agendar carona", None))
        self.pedir.setText(_translate("MainWindow", "Pedir carona", None))
        self.perfil.setText(_translate("MainWindow", "Alterar perfil", None))
        self.remover.setText(_translate("MainWindow", "Remover carona pedida", None))
        self.remover2.setText(_translate("MainWindow", "Remover carona oferecida", None))
        self.logout.setText(_translate("MainWindow", "Log Out", None))


    def abrirpedir(self):
        self.MainWindow = pedircarona.Ui_MainWindow
        telapedir = QtGui.QMainWindow()
        ui = pedircarona.Ui_MainWindow()
        ui.setupUi(telapedir, self.usuarios, self.nome_completo, self.telefone, self.email)
        telapedir.show()
        sys.exit(app.exec_())

    def abriragendar(self):
        self.MainWindow = agendarcarona.Ui_MainWindow
        tela_agendar = QtGui.QMainWindow()
        ui = agendarcarona.Ui_MainWindow()
        ui.setupUi(tela_agendar, self.usuarios, self.nome_completo, self.telefone, self.email)
        tela_agendar.show()
        sys.exit(app.exec_())

    def removerpedido(self):
        fb = firebase.FirebaseApplication('https://caronas.firebaseio.com')
        pedidos = fb.get('/Pedidos', None)
        
        if self.usuarios in pedidos:
            dlg = QtGui.QMessageBox(None)
            dlg.setWindowTitle("Confirmação")
            dlg.setIcon(QtGui.QMessageBox.Question)
            dlg.setText("Deseja cancelar seu pedido?")
            dlg.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            dlg.setDefaultButton(QtGui.QMessageBox.Yes)
            dlg.setEscapeButton(QtGui.QMessageBox.No)
            resultado = dlg.exec_()
            if resultado == QtGui.QMessageBox.Yes:
                fb.delete('Pedidos', self.usuarios)
                dlg = QtGui.QMessageBox(None)
                dlg.setWindowTitle("Cancelamento")
                dlg.setIcon(QtGui.QMessageBox.Information)
                dlg.setText("Pedido cancelado com sucesso!")
                dlg.exec_()
        else:
            dlg = QtGui.QMessageBox(None)
            dlg.setWindowTitle("Cancelamento")
            dlg.setIcon(QtGui.QMessageBox.Information)
            dlg.setText("Não existe um pedido de carona.")
            dlg.exec_()


    def removeroferta(self):
        fb = firebase.FirebaseApplication('https://caronas.firebaseio.com')
        ofertas = fb.get("/Ofertas", None)
         
        if self.usuarios in ofertas:
            dlg = QtGui.QMessageBox(None)
            dlg.setWindowTitle("Confirmação")
            dlg.setIcon(QtGui.QMessageBox.Question)
            dlg.setText("Deseja cancelar sua oferta?")
            dlg.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            dlg.setDefaultButton(QtGui.QMessageBox.Yes)
            dlg.setEscapeButton(QtGui.QMessageBox.No)
            resultado = dlg.exec_()
            if resultado == QtGui.QMessageBox.Yes:
                fb.delete('Ofertas', self.usuarios)
                dlg = QtGui.QMessageBox(None)
                dlg.setWindowTitle("Cancelamento")
                dlg.setIcon(QtGui.QMessageBox.Information)
                dlg.setText("Oferta cancelada com sucesso!")
                dlg.exec_()
        else:
            dlg = QtGui.QMessageBox(None)
            dlg.setWindowTitle("Cancelamento")
            dlg.setIcon(QtGui.QMessageBox.Information)
            dlg.setText("Não existe uma carona agendada.")
            dlg.exec_()

    def abrirperfil(self):
        self.MainWindow = perfil.Ui_MainWindow
        tela_perfil = QtGui.QMainWindow()
        ui = perfil.Ui_MainWindow()
        ui.setupUi(tela_perfil, self.usuarios, self.nome_completo, self.telefone, self.email)
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
    ui.setupUi(MainWindow, "usuario", "nome", "email", "tel")
    MainWindow.show()
    sys.exit(app.exec_())

