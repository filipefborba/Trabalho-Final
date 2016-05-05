# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caronas.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import tela_cadastro, telaprincipal

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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(844, 559)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.login = QtGui.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(270, 240, 300, 50))
        self.login.setObjectName(_fromUtf8("login"))
        self.login.clicked.connect(self.abrirlogin)

        self.cadastro = QtGui.QPushButton(self.centralwidget)
        self.cadastro.setGeometry(QtCore.QRect(270, 340, 300, 50))
        self.cadastro.setObjectName(_fromUtf8("cadastro"))
        self.cadastro.clicked.connect(self.abrircadastro)

        self.caronasinsperlabel = QtGui.QLabel(self.centralwidget)
        self.caronasinsperlabel.setGeometry(QtCore.QRect(170, 40, 521, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(60)
        self.caronasinsperlabel.setFont(font)
        self.caronasinsperlabel.setObjectName(_fromUtf8("caronasinsperlabel"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.login.setText(_translate("MainWindow", "Login", None))
        self.cadastro.setText(_translate("MainWindow", "Cadastre-se", None))
        self.caronasinsperlabel.setText(_translate("MainWindow", "Caronas Insper", None))

    def abrircadastro(self):
        self.MainWindow = tela_cadastro.Ui_MainWindow
        teladecadastro = QtGui.QMainWindow()
        ui = tela_cadastro.Ui_MainWindow()
        ui.setupUi(teladecadastro)
        teladecadastro.show()
        sys.exit(app.exec_())

    def abrirlogin(self):
        self.MainWindow = tela_cadastro.Ui_MainWindow
        teladelogin = QtGui.QMainWindow()
        ui = telaprincipal.Ui_MainWindow()
        ui.setupUi(teladelogin)
        teladelogin.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())