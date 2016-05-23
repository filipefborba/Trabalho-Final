# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sobre.ui'
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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(844, 559)
        MainWindow.setFixedSize(844,559)
        MainWindow.setWindowIcon(QtGui.QIcon("Fotos/carro.jpg"))

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

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.oprojetolabel = QtGui.QLabel(self.centralwidget)
        self.oprojetolabel.setGeometry(QtCore.QRect(310, 10, 211, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(36)
        self.oprojetolabel.setFont(font)
        self.oprojetolabel.setObjectName(_fromUtf8("oprojetolabel"))

        self.borba = QtGui.QLabel(self.centralwidget)
        self.borba.setGeometry(QtCore.QRect(350, 490, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(16)
        self.borba.setFont(font)
        self.borba.setObjectName(_fromUtf8("borba"))

        self.noto = QtGui.QLabel(self.centralwidget)
        self.noto.setGeometry(QtCore.QRect(650, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(16)
        self.noto.setFont(font)
        self.noto.setObjectName(_fromUtf8("noto"))

        self.andre = QtGui.QLabel(self.centralwidget)
        self.andre.setGeometry(QtCore.QRect(50, 490, 181, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(16)
        self.andre.setFont(font)
        self.andre.setObjectName(_fromUtf8("andre"))

        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 90, 621, 111))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))

        self.fotoborba = QtGui.QLabel(self.centralwidget)
        self.fotoborba.setGeometry(QtCore.QRect(300, 250, 221, 231))
        self.fotoborba.setText(_fromUtf8(""))
        self.fotoborba.setPixmap(QtGui.QPixmap(_fromUtf8("Fotos/borba.jpg")))
        self.fotoborba.setScaledContents(True)
        self.fotoborba.setObjectName(_fromUtf8("fotoborba"))

        self.fotonoto = QtGui.QLabel(self.centralwidget)
        self.fotonoto.setGeometry(QtCore.QRect(600, 220, 191, 261))
        self.fotonoto.setText(_fromUtf8(""))
        self.fotonoto.setPixmap(QtGui.QPixmap(_fromUtf8("Fotos/luca.jpg")))
        self.fotonoto.setScaledContents(True)
        self.fotonoto.setObjectName(_fromUtf8("fotonoto"))

        self.fotodeco = QtGui.QLabel(self.centralwidget)
        self.fotodeco.setGeometry(QtCore.QRect(20, 240, 231, 241))
        self.fotodeco.setText(_fromUtf8(""))
        self.fotodeco.setPixmap(QtGui.QPixmap(_fromUtf8("Fotos/andre.jpg")))
        self.fotodeco.setScaledContents(True)
        self.fotodeco.setObjectName(_fromUtf8("fotodeco"))

        self.voltar = QtGui.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(0, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.voltar.setFont(font)
        self.voltar.setObjectName(_fromUtf8("voltar"))
        self.voltar.clicked.connect(self.abrircaronas)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Caronas Insper", None))
        self.oprojetolabel.setText(_translate("MainWindow", "O projeto", None))
        self.borba.setText(_translate("MainWindow", "Filipe Borba", None))
        self.noto.setText(_translate("MainWindow", "Luca Noto", None))
        self.andre.setText(_translate("MainWindow", "André Ejzenmesser", None))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Olá! Obrigado por utilizar nosso aplicativo!\n"
"\n"
"Este é um projeto desenvolvido para a disciplina Design de Softwares do 1º Semestre do Insper (Instituto de Ensino e Pesquisa).\n"
"\n"
"Quando surgiu a ideia de desenvolver este aplicativo, tinhamos como objetivo ajudar e incentivar os alunos do Insper a pegar caronas uns com os outros, diminuindo os carros nas ruas e estabelecendo novas amizades.", None))
        self.voltar.setText(_translate("MainWindow", "Voltar", None))

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

