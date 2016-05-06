# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pedircarona.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import principal

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

        ##########################LABELS###################################
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(170, 50, 531, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(28)
        self.titulo.setFont(font)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.destinolabel = QtGui.QLabel(self.centralwidget)
        self.destinolabel.setGeometry(QtCore.QRect(50, 310, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.destinolabel.setFont(font)
        self.destinolabel.setObjectName(_fromUtf8("destinolabel"))
        self.partidalabel = QtGui.QLabel(self.centralwidget)
        self.partidalabel.setGeometry(QtCore.QRect(50, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.partidalabel.setFont(font)
        self.partidalabel.setObjectName(_fromUtf8("partidalabel"))
        #############################FIM DAS LABELS########################


        self.partida = QtGui.QComboBox(self.centralwidget)
        self.partida.setGeometry(QtCore.QRect(200, 220, 411, 22))
        self.partida.setEditable(False)
        self.partida.setObjectName(_fromUtf8("partida"))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))

        self.destino = QtGui.QComboBox(self.centralwidget)
        self.destino.setGeometry(QtCore.QRect(200, 320, 411, 22))
        self.destino.setEditable(False)
        self.destino.setObjectName(_fromUtf8("destino"))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))

        self.lugares = QtGui.QComboBox(self.centralwidget)
        self.lugares.setGeometry(QtCore.QRect(200, 400, 411, 22))
        self.lugares.setEditable(True)
        self.lugares.setObjectName(_fromUtf8("lugares"))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))

        self.lugareslabel = QtGui.QLabel(self.centralwidget)
        self.lugareslabel.setGeometry(QtCore.QRect(50, 390, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.lugareslabel.setFont(font)
        self.lugareslabel.setObjectName(_fromUtf8("lugareslabel"))

        self.voltar = QtGui.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(170, 460, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.voltar.setFont(font)
        self.voltar.setObjectName(_fromUtf8("voltar"))
        self.voltar.clicked.connect(self.abrirprincipal)

        self.confirmar = QtGui.QPushButton(self.centralwidget)
        self.confirmar.setGeometry(QtCore.QRect(530, 460, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.confirmar.setFont(font)
        self.confirmar.setObjectName(_fromUtf8("confirmar"))


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.titulo.setText(_translate("MainWindow", "Selecione suas localizações:", None))
        self.destinolabel.setText(_translate("MainWindow", "Local de Destino:", None))
        self.partidalabel.setText(_translate("MainWindow", "Local de Partida:", None))
        self.partida.setItemText(0, _translate("MainWindow", "Jardins", None))
        self.partida.setItemText(1, _translate("MainWindow", "Itaim Bibi", None))
        self.partida.setItemText(2, _translate("MainWindow", "Aclimação", None))
        self.partida.setItemText(3, _translate("MainWindow", "Perdizes", None))
        self.partida.setItemText(4, _translate("MainWindow", "Morumbi", None))
        self.partida.setItemText(5, _translate("MainWindow", "Insper", None))
        self.destino.setItemText(0, _translate("MainWindow", "Jardins", None))
        self.destino.setItemText(1, _translate("MainWindow", "Itaim Bibi", None))
        self.destino.setItemText(2, _translate("MainWindow", "Aclimação", None))
        self.destino.setItemText(3, _translate("MainWindow", "Perdizes", None))
        self.destino.setItemText(4, _translate("MainWindow", "Morumbi", None))
        self.destino.setItemText(5, _translate("MainWindow", "Insper", None))
        self.voltar.setText(_translate("MainWindow", "Voltar", None))
        self.confirmar.setText(_translate("MainWindow", "Confirmar", None))
        self.lugares.setItemText(0, _translate("MainWindow", "1", None))
        self.lugares.setItemText(1, _translate("MainWindow", "2", None))
        self.lugares.setItemText(2, _translate("MainWindow", "3", None))
        self.lugares.setItemText(3, _translate("MainWindow", "4", None))
        self.lugareslabel.setText(_translate("MainWindow", "Lugares disponíveis:", None))


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
