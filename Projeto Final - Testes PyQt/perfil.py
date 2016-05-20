# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perfil.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import principal, login
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
    def setupUi(self, MainWindow, usuarios):
        self.usuarios = usuarios


        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 592)
        MainWindow.setFixedSize(801,592)
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

#########LABELS#######################################
        self.nomelabel = QtGui.QLabel(self.centralwidget)
        self.nomelabel.setGeometry(QtCore.QRect(40, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.nomelabel.setFont(font)
        self.nomelabel.setObjectName(_fromUtf8("nomelabel"))
        self.celularlabel = QtGui.QLabel(self.centralwidget)
        self.celularlabel.setGeometry(QtCore.QRect(40, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.celularlabel.setFont(font)
        self.celularlabel.setObjectName(_fromUtf8("celularlabel"))
        self.emaillabel = QtGui.QLabel(self.centralwidget)
        self.emaillabel.setGeometry(QtCore.QRect(40, 240, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.emaillabel.setFont(font)
        self.emaillabel.setObjectName(_fromUtf8("emaillabel"))
        self.usuariolabel = QtGui.QLabel(self.centralwidget)
        self.usuariolabel.setGeometry(QtCore.QRect(40, 300, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.usuariolabel.setFont(font)
        self.usuariolabel.setObjectName(_fromUtf8("usuariolabel"))
        self.senhalabel = QtGui.QLabel(self.centralwidget)
        self.senhalabel.setGeometry(QtCore.QRect(40, 360, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.senhalabel.setFont(font)
        self.senhalabel.setObjectName(_fromUtf8("senhalabel"))
        self.confirmarsenhalabel = QtGui.QLabel(self.centralwidget)
        self.confirmarsenhalabel.setGeometry(QtCore.QRect(40, 420, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.confirmarsenhalabel.setFont(font)
        self.confirmarsenhalabel.setObjectName(_fromUtf8("confirmarsenhalabel"))
        self.alterarperfiltitulo = QtGui.QLabel(self.centralwidget)
        self.alterarperfiltitulo.setGeometry(QtCore.QRect(200, 40, 421, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(48)
        self.alterarperfiltitulo.setFont(font)
        self.alterarperfiltitulo.setObjectName(_fromUtf8("alterarperfiltitulo"))
        ###################FIM DAS LABELS##################################

        dados = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')

        self.nomeinput = QtGui.QLineEdit(self.centralwidget)
        self.nomeinput.setGeometry(QtCore.QRect(170, 130, 491, 20))
        self.nomeinput.setObjectName(_fromUtf8("nomeinput"))
        self.nomeinput.setText(dados.get(self.usuarios, 'Nome'))

        self.celularinput = QtGui.QLineEdit(self.centralwidget)
        self.celularinput.setGeometry(QtCore.QRect(170, 190, 491, 20))
        self.celularinput.setInputMask(_fromUtf8(""))
        self.celularinput.setText(_fromUtf8(""))
        self.celularinput.setMaxLength(11)
        self.celularinput.setObjectName(_fromUtf8("celularinput"))
        self.celularinput.setText(dados.get(self.usuarios, 'telefone'))

        self.emailinput = QtGui.QLineEdit(self.centralwidget)
        self.emailinput.setGeometry(QtCore.QRect(170, 250, 491, 20))
        self.emailinput.setObjectName(_fromUtf8("emailinput"))
        self.emailinput.setText(dados.get(self.usuarios, 'email'))

        self.usuarioinput = QtGui.QLineEdit(self.centralwidget)
        self.usuarioinput.setGeometry(QtCore.QRect(170, 310, 491, 20))
        self.usuarioinput.setObjectName(_fromUtf8("usuarioinput"))
        self.usuarioinput.setReadOnly(True)
        self.usuarioinput.setText(self.usuarios)

        self.senhainput = QtGui.QLineEdit(self.centralwidget)
        self.senhainput.setGeometry(QtCore.QRect(170, 370, 491, 20))
        self.senhainput.setEchoMode(QtGui.QLineEdit.Password)
        self.senhainput.setObjectName(_fromUtf8("senhainput"))
        self.senhainput.setText(dados.get(self.usuarios, 'senha'))

        self.confirmarsenhainput = QtGui.QLineEdit(self.centralwidget)
        self.confirmarsenhainput.setGeometry(QtCore.QRect(170, 430, 491, 20))
        self.confirmarsenhainput.setEchoMode(QtGui.QLineEdit.Password)
        self.confirmarsenhainput.setObjectName(_fromUtf8("confirmarsenhainput"))
        self.confirmarsenhainput.setText(dados.get(self.usuarios, 'senha'))

        self.voltar = QtGui.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(220, 480, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.voltar.setFont(font)
        self.voltar.setObjectName(_fromUtf8("voltar"))
        self.voltar.clicked.connect(self.abrirprincipal)

        self.confirmar = QtGui.QPushButton(self.centralwidget)
        self.confirmar.setGeometry(QtCore.QRect(510, 480, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.confirmar.setFont(font)
        self.confirmar.setObjectName(_fromUtf8("confirmar"))
        self.confirmar.clicked.connect(self.registrarperfil)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Caronas Insper", None))
        self.nomelabel.setText(_translate("MainWindow", "Nome completo:", None))
        self.celularlabel.setText(_translate("MainWindow", "Nº de celular:", None))
        self.emaillabel.setText(_translate("MainWindow", "E-mail:", None))
        self.usuariolabel.setText(_translate("MainWindow", "Usuário:", None))
        self.senhalabel.setText(_translate("MainWindow", "Senha:", None))
        self.confirmarsenhalabel.setText(_translate("MainWindow", "Confirmar senha:", None))
        self.alterarperfiltitulo.setText(_translate("MainWindow", "Alterar Perfil", None))
        self.voltar.setText(_translate("MainWindow", "Voltar", None))
        self.confirmar.setText(_translate("MainWindow", "Confirmar", None))


    def registrarperfil(self):    
        if self.senhainput.text() == self.confirmarsenhainput.text() and self.nomeinput.text() != '' and self.emailinput.text() != '' and self.celularinput.text() != '' and self.celularinput.text() != '' and self.usuarioinput.text() != '':    
            dlg = QtGui.QMessageBox(None)
            dlg.setWindowTitle("Confirmação")
            dlg.setIcon(QtGui.QMessageBox.Question)
            dlg.setText("Deseja confirmar as informações?")
            dlg.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            dlg.setDefaultButton(QtGui.QMessageBox.Yes)
            dlg.setEscapeButton(QtGui.QMessageBox.No)
            resultado = dlg.exec_()

            if resultado == QtGui.QMessageBox.Yes:
                
                fb = firebase.FirebaseApplication('https://caronas.firebaseio.com')
                dicionario = {'Nome': self.nomeinput.text(),'email': self.emailinput.text(), 'telefone': self.celularinput.text(), 'senha': self.senhainput.text()}
                fb.put('Users', self.usuarioinput.text(), dicionario)
                self.MainWindow = principal.Ui_MainWindow
                tela_principal = QtGui.QMainWindow()
                ui = principal.Ui_MainWindow()
                ui.setupUi(tela_principal, self.usuarios)
                tela_principal.show()
                sys.exit(app.exec_())

        else:
            dlg2 = QtGui.QMessageBox(None)
            dlg2.setWindowTitle("Erro")
            dlg2.setIcon(QtGui.QMessageBox.Warning)
            dlg2.setText("Preencha os campos corretamente, por favor.")
            dlg2.exec_()


    def abrirprincipal(self):
        self.MainWindow = principal.Ui_MainWindow
        tela_principal = QtGui.QMainWindow()
        ui = principal.Ui_MainWindow()
        ui.setupUi(tela_principal)
        tela_principal.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

