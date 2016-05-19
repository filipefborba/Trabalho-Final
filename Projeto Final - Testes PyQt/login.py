# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telalogin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from firebase import firebase
import principal, caronas

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
        MainWindow.resize(796, 553)
        MainWindow.setFixedSize(796, 553)
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

        #Título grande
        self.caronasinsperlabel = QtGui.QLabel(self.centralwidget)
        self.caronasinsperlabel.setGeometry(QtCore.QRect(140, 30, 521, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(60)

        self.caronasinsperlabel.setFont(font)
        self.caronasinsperlabel.setObjectName(_fromUtf8("caronasinsperlabel"))
        self.senhalabel = QtGui.QLabel(self.centralwidget)
        self.senhalabel.setGeometry(QtCore.QRect(40, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)

        self.senhalabel.setFont(font)
        self.senhalabel.setObjectName(_fromUtf8("senhalabel"))

        self.usuarioinput = QtGui.QLineEdit(self.centralwidget)
        self.usuarioinput.setGeometry(QtCore.QRect(170, 260, 491, 20))
        self.usuarioinput.setObjectName(_fromUtf8("usuarioinput"))
        self.usuarioinput.setPlaceholderText("Nome de Usuário")
        self.usuarioinput.returnPressed.connect(self.abrirprincipal)

        self.senhainput = QtGui.QLineEdit(self.centralwidget)
        self.senhainput.setGeometry(QtCore.QRect(170, 320, 491, 20))
        self.senhainput.setEchoMode(QtGui.QLineEdit.Password)
        self.senhainput.setObjectName(_fromUtf8("senhainput"))
        self.senhainput.setPlaceholderText("Senha")
        self.senhainput.returnPressed.connect(self.abrirprincipal)

        self.voltar = QtGui.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(160, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.voltar.setFont(font)
        self.voltar.setObjectName(_fromUtf8("voltar"))
        self.voltar.clicked.connect(self.abrircaronas)

        self.usuariolabel = QtGui.QLabel(self.centralwidget)
        self.usuariolabel.setGeometry(QtCore.QRect(40, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)

        self.usuariolabel.setFont(font)
        self.usuariolabel.setObjectName(_fromUtf8("usuariolabel"))

        self.confirmar = QtGui.QPushButton(self.centralwidget)
        self.confirmar.setGeometry(QtCore.QRect(520, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.confirmar.setFont(font)
        self.confirmar.setObjectName(_fromUtf8("confirmar"))
        self.confirmar.clicked.connect(self.abrirprincipal)
        self.confirmar.setAutoDefault(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Caronas Insper", None))
        self.caronasinsperlabel.setText(_translate("MainWindow", "Caronas Insper", None))
        self.senhalabel.setText(_translate("MainWindow", "Senha:", None))
        self.voltar.setText(_translate("MainWindow", "Voltar", None))
        self.usuariolabel.setText(_translate("MainWindow", "Usuário:", None))
        self.confirmar.setText(_translate("MainWindow", "Confirmar", None))

    def abrirprincipal(self):
        self.usuario = self.usuarioinput.text()
        self.usuarios = self.usuario
        
        fb = firebase.FirebaseApplication('https://caronas.firebaseio.com')
        pessoas = fb.get('/Users', None)
        
        if self.usuario in pessoas:
            
            fb2 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')
            self.senha_pra_conferir = fb2.get(self.usuario, 'senha')
            
            if self.senha_pra_conferir == self.senhainput.text():
                self.MainWindow = principal.Ui_MainWindow
                tela_principal = QtGui.QMainWindow()
                ui = principal.Ui_MainWindow()
                ui.setupUi(tela_principal)
                tela_principal.show()
                sys.exit(app.exec_())

                self.nome_completo = fb2.get(self.usuario, 'Nome')
                self.telefone = fb2.get(self.usuario, 'telefone')
                self.email = fb2.get(self.usuario, 'email')

            else:
                dlg = QtGui.QMessageBox(None)
                dlg.setWindowTitle("Erro")
                dlg.setIcon(QtGui.QMessageBox.Warning)
                dlg.setText("Senha incorreta.")
                dlg.exec_()
            
        else:
            dlg2 = QtGui.QMessageBox(None)
            dlg2.setWindowTitle("Erro")
            dlg2.setIcon(QtGui.QMessageBox.Warning)
            dlg2.setText("Usuário inexistente.")
            dlg2.exec_()
        

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

