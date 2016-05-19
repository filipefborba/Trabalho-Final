# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pedircarona.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from firebase import firebase
import principal, login

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
        ##########################################################

        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(170, 50, 531, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(28)
        self.titulo.setFont(font)
        self.titulo.setObjectName(_fromUtf8("titulo"))

        self.destinolabel = QtGui.QLabel(self.centralwidget)
        self.destinolabel.setGeometry(QtCore.QRect(30, 230, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.destinolabel.setFont(font)
        self.destinolabel.setObjectName(_fromUtf8("destinolabel"))

        self.partidalabel = QtGui.QLabel(self.centralwidget)
        self.partidalabel.setGeometry(QtCore.QRect(30, 150, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.partidalabel.setFont(font)
        self.partidalabel.setObjectName(_fromUtf8("partidalabel"))

        self.partida = QtGui.QComboBox(self.centralwidget)
        self.partida.setGeometry(QtCore.QRect(180, 160, 411, 22))
        self.partida.setEditable(False)
        self.partida.setObjectName(_fromUtf8("partida"))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))
        self.partida.addItem(_fromUtf8(""))

        self.destino = QtGui.QComboBox(self.centralwidget)
        self.destino.setGeometry(QtCore.QRect(180, 240, 411, 22))
        self.destino.setEditable(False)
        self.destino.setObjectName(_fromUtf8("destino"))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))
        self.destino.addItem(_fromUtf8(""))

        self.voltar = QtGui.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(170, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.voltar.setFont(font)
        self.voltar.setObjectName(_fromUtf8("voltar"))
        self.voltar.clicked.connect(self.abrirprincipal)

        self.confirmar = QtGui.QPushButton(self.centralwidget)
        self.confirmar.setGeometry(QtCore.QRect(530, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.confirmar.setFont(font)
        self.confirmar.setObjectName(_fromUtf8("confirmar"))
        self.confirmar.clicked.connect(self.registrarpedido)

        self.datalabel = QtGui.QLabel(self.centralwidget)
        self.datalabel.setGeometry(QtCore.QRect(30, 300, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.datalabel.setFont(font)
        self.datalabel.setObjectName(_fromUtf8("datalabel"))

        self.lugareslabel = QtGui.QLabel(self.centralwidget)
        self.lugareslabel.setGeometry(QtCore.QRect(30, 380, 181, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.lugareslabel.setFont(font)
        self.lugareslabel.setObjectName(_fromUtf8("lugareslabel"))

        self.lugares = QtGui.QComboBox(self.centralwidget)
        self.lugares.setGeometry(QtCore.QRect(180, 390, 411, 22))
        self.lugares.setEditable(False)
        self.lugares.setMaxVisibleItems(4)
        self.lugares.setObjectName(_fromUtf8("lugares"))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))

        self.data = QtGui.QDateEdit(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(180, 310, 110, 22))
        self.data.setCalendarPopup(True)
        self.data.setObjectName(_fromUtf8("data"))
        self.data.setDate(QtCore.QDate.currentDate())
        self.data.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2016, 12, 31), QtCore.QTime(23, 59, 59)))
        self.data.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate.currentDate(), QtCore.QTime(0, 0, 0)))

        self.horariolabel = QtGui.QLabel(self.centralwidget)
        self.horariolabel.setGeometry(QtCore.QRect(340, 300, 71, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.horariolabel.setFont(font)
        self.horariolabel.setObjectName(_fromUtf8("horariolabel"))

        self.horario = QtGui.QTimeEdit(self.centralwidget)
        self.horario.setGeometry(QtCore.QRect(470, 310, 118, 22))
        self.horario.setMaximumTime(QtCore.QTime(23, 0, 0))
        self.horario.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.horario.setCalendarPopup(False)
        self.horario.setObjectName(_fromUtf8("horario"))


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lugares.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Caronas Insper", None))
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
        self.datalabel.setText(_translate("MainWindow", "Data:", None))
        self.lugareslabel.setText(_translate("MainWindow", "Lugares necessários:", None))
        self.lugares.setItemText(0, _translate("MainWindow", "1", None))
        self.lugares.setItemText(1, _translate("MainWindow", "2", None))
        self.lugares.setItemText(2, _translate("MainWindow", "3", None))
        self.lugares.setItemText(3, _translate("MainWindow", "4", None))
        self.horariolabel.setText(_translate("MainWindow", "Horário:", None))
        self.horario.setDisplayFormat(_translate("MainWindow", "HH:mm", None))
        self.data.setDisplayFormat(_translate("MainWindow","dd/MM", None))

    def registrarpedido(self):
        dlg = QtGui.QMessageBox(None)
        dlg.setWindowTitle("Confirmação")
        dlg.setIcon(QtGui.QMessageBox.Question)
        dlg.setText("Deseja confirmar o pedido?")
        dlg.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        dlg.setDefaultButton(QtGui.QMessageBox.Yes)
        dlg.setEscapeButton(QtGui.QMessageBox.No)
        resultado = dlg.exec_()

        #self.usuarios = login.Ui_MainWindow.abrirprincipal(self).usuarios
            
        if resultado == QtGui.QMessageBox.Yes:
            fb = firebase.FirebaseApplication('https://caronas.firebaseio.com', None)
            dicionario = {'Horário': "horario", 'Data': "data", 'Local de Saída': self.partida.currentText(), 'Local de Chegada': self.destino.currentText(), 'Lugares Necessários': self.lugares.currentText()}
            fb.put('/Pedidos', "filipefb", dicionario)
            
            ofertas = fb.get('Ofertas', None)
            
            fb2 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Pedidos/')
            fb3 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Ofertas/')
            fb4 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')

            lugar_saida_pedido = fb2.get("filipefb", 'Local de Saída')
            lugar_chegada_pedido = fb2.get("filipefb", 'Local de Chegada')
            horario_pedido = fb2.get("filipefb", 'Horário')
            lugares_necessarios_pedido = fb2.get("filipefb", 'Lugares Necessários')
            
            for motorista in ofertas:
                lugar_saida_oferta = fb3.get(motorista, 'Local de Saída')
                lugar_chegada_oferta = fb3.get(motorista, 'Local de Chegada')
                horario_oferta = fb3.get(motorista, 'Horário')
                lugares_necessarios_oferta = fb3.get(motorista, 'Lugares Necessários')
                
                if lugar_saida_pedido == lugar_saida_oferta and lugar_chegada_pedido == lugar_chegada_oferta and lugares_necessarios_pedido <= lugares_necessarios_oferta and horario_pedido == horario_oferta:
                    nome = fb4.get(motorista,'Nome')
                    celular = fb4.get(motorista, 'telefone')
                    email = fb4.get(motorista, 'email')
                                        
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = self.email
    
                    msg = 'Seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para combinarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(nome, celular, email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = email
    
                    msg = 'Seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para marcarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(self.nome_completo, self.telefone, self.email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    
                    fb.delete('/Pedidos', self.usuarios)
                    fb.delete('/Ofertas', motorista)
                    
                    dlg = QtGui.QMessageBox(None)
                    dlg.setWindowTitle("Carona")
                    dlg.setIcon(QtGui.QMessageBox.Information)
                    dlg.setText("As informações de quem te dará carona estão no seu e-mail!")
                    dlg.exec_()
                    break
            else:
                dlg = QtGui.QMessageBox(None)
                dlg.setWindowTitle("Carona")
                dlg.setIcon(QtGui.QMessageBox.Information)
                dlg.setText("Não existem caronas no momento. Quando existir alguém, você será notificado por email!")
                dlg.exec_()
                                
            self.MainWindow = principal.Ui_MainWindow
            tela_principal = QtGui.QMainWindow()
            ui = principal.Ui_MainWindow()
            ui.setupUi(tela_principal)
            tela_principal.show()
            sys.exit(app.exec_())

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

