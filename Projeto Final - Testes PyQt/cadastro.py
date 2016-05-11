# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        #Frame da Janela
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 592)
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
        self.cadastrotitulo = QtGui.QLabel(self.centralwidget)
        self.cadastrotitulo.setGeometry(QtCore.QRect(260, 40, 271, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(48)
        self.cadastrotitulo.setFont(font)
        self.cadastrotitulo.setObjectName(_fromUtf8("cadastrotitulo"))
        ###################FIM DAS LABELS###################################


        self.nomeinput = QtGui.QLineEdit(self.centralwidget)
        self.nomeinput.setGeometry(QtCore.QRect(170, 130, 491, 20))
        self.nomeinput.setObjectName(_fromUtf8("nomeinput"))

        self.celularinput = QtGui.QLineEdit(self.centralwidget)
        self.celularinput.setGeometry(QtCore.QRect(170, 190, 491, 20))
        self.celularinput.setInputMask(_fromUtf8(""))
        self.celularinput.setText(_fromUtf8(""))
        self.celularinput.setMaxLength(11)
        self.celularinput.setObjectName(_fromUtf8("celularinput"))

        self.emailinput = QtGui.QLineEdit(self.centralwidget)
        self.emailinput.setGeometry(QtCore.QRect(170, 250, 491, 20))
        self.emailinput.setObjectName(_fromUtf8("emailinput"))

        self.usuarioinput = QtGui.QLineEdit(self.centralwidget)
        self.usuarioinput.setGeometry(QtCore.QRect(170, 310, 491, 20))
        self.usuarioinput.setObjectName(_fromUtf8("usuarioinput"))

        self.senhainput = QtGui.QLineEdit(self.centralwidget)
        self.senhainput.setGeometry(QtCore.QRect(170, 370, 491, 20))
        self.senhainput.setEchoMode(QtGui.QLineEdit.Password)
        self.senhainput.setObjectName(_fromUtf8("senhainput"))

        self.confirmarsenhainput = QtGui.QLineEdit(self.centralwidget)
        self.confirmarsenhainput.setGeometry(QtCore.QRect(170, 430, 491, 20))
        self.confirmarsenhainput.setEchoMode(QtGui.QLineEdit.Password)
        self.confirmarsenhainput.setObjectName(_fromUtf8("confirmarsenhainput"))

        self.voltar = QtGui.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(220, 480, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.voltar.setFont(font)
        self.voltar.setObjectName(_fromUtf8("voltar"))
        self.voltar.clicked.connect(self.abrircaronas)

        self.confirmar = QtGui.QPushButton(self.centralwidget)
        self.confirmar.setGeometry(QtCore.QRect(510, 480, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.confirmar.setFont(font)
        self.confirmar.setObjectName(_fromUtf8("confirmar"))
        self.confirmar.clicked.connect(self.registrarcadastro)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.nomelabel.setText(_translate("MainWindow", "Nome completo:", None))
        self.celularlabel.setText(_translate("MainWindow", "Nº de celular: ", None))
        self.emaillabel.setText(_translate("MainWindow", "E-mail:@.com", None))
        self.usuariolabel.setText(_translate("MainWindow", "Usuário:", None))
        self.senhalabel.setText(_translate("MainWindow", "Senha:", None))
        self.confirmarsenhalabel.setText(_translate("MainWindow", "Confirmar senha:", None))
        self.cadastrotitulo.setText(_translate("MainWindow", "Cadastro", None))
        self.voltar.setText(_translate("MainWindow", "Voltar", None))
        self.confirmar.setText(_translate("MainWindow", "Confirmar", None))

    def registrarcadastro(self):
        pass


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

