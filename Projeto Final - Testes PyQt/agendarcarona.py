# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agendarcarona.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import principal, smtplib
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
        bairros = sorted(['','Cerqueira César','Vila Leopoldina','Vila Olímpia','Higienópolis','Morumbi','Jardins','Itaim','Jardim Paulista','Moema','Osasco','Itaquera','Alphaville','Pinheiros', 'Alto de Pinheiros', 'Jardim Paulistano', 'Jardim Europa', 'Paraíso','Perdizes','Campo Belo','Consolação','Aclimação','Chácara Inglesa','Chácara Klabin','Butantã'])
        i = 0
        horarios = ['', '0h00','0h30','1h00','1h30','2h00','2h30','3h00','3h30','4h00','4h30','5h00','5h30','6h00','6h30','7h00','7h30','8h00','8h30','9h00','9h30','10h00','10h30','11h00','11h30','12h00','12h30','13h00','13h30','14h00','14h30','15h00','16h00','16h30','17h00','17h30','18h00','18h30','19h00','19h30','20h00','20h30','21h00','21h30','22h00','22h30','23h00','23h30']
        dia = ['','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        mes = ['','1','2','3','4','5','6','7','8','9','10','11','12']
        i=0

        #Frame da janela
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
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

        self.destinolabel = QtGui.QLabel(self.centralwidget)
        self.destinolabel.setGeometry(QtCore.QRect(40, 230, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.destinolabel.setFont(font)
        self.destinolabel.setObjectName(_fromUtf8("destinolabel"))

        self.destino = QtGui.QComboBox(self.centralwidget)
        self.destino.setGeometry(QtCore.QRect(190, 240, 411, 22))
        self.destino.setEditable(False)
        self.destino.setObjectName(_fromUtf8("destino"))

        self.partida = QtGui.QComboBox(self.centralwidget)
        self.partida.setGeometry(QtCore.QRect(190, 140, 411, 22))
        self.partida.setEditable(False)
        self.partida.setObjectName(_fromUtf8("partida"))

        for i in range(len(bairros)):
            self.partida.addItem(_fromUtf8(""))
            self.destino.addItem(_fromUtf8(""))

        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(240, 40, 371, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(28)
        self.titulo.setFont(font)
        self.titulo.setObjectName(_fromUtf8("titulo"))

        self.partidalabel = QtGui.QLabel(self.centralwidget)
        self.partidalabel.setGeometry(QtCore.QRect(40, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.partidalabel.setFont(font)
        self.partidalabel.setObjectName(_fromUtf8("partidalabel"))

        self.horariolabel = QtGui.QLabel(self.centralwidget)
        self.horariolabel.setGeometry(QtCore.QRect(40, 320, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.horariolabel.setFont(font)
        self.horariolabel.setObjectName(_fromUtf8("horariolabel"))

        self.horario = QtGui.QComboBox(self.centralwidget)
        self.horario.setGeometry(QtCore.QRect(190, 330, 110, 22))
        self.horario.setEditable(False)
        self.horario.setObjectName(_fromUtf8("horario"))
        for i in range(len(horarios)):
            self.horario.addItem(_fromUtf8(""))

        self.datalabel = QtGui.QLabel(self.centralwidget)
        self.datalabel.setGeometry(QtCore.QRect(390, 320, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.datalabel.setFont(font)
        self.datalabel.setObjectName(_fromUtf8("datalabel"))

        self.dia = QtGui.QComboBox(self.centralwidget)
        self.dia.setGeometry(QtCore.QRect(440, 330, 50, 22))
        self.dia.setEditable(False)
        self.dia.setObjectName(_fromUtf8("dia"))
        for i in range(len(dia)):
            self.dia.addItem(_fromUtf8(""))

        self.mes = QtGui.QComboBox(self.centralwidget)
        self.mes.setGeometry(QtCore.QRect(500, 330, 50, 22))
        self.mes.setEditable(False)
        self.mes.setObjectName(_fromUtf8("mes"))
        for i in range(len(mes)):
            self.mes.addItem(_fromUtf8(""))

        self.voltar = QtGui.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(150, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.voltar.setFont(font)
        self.voltar.setObjectName(_fromUtf8("voltar"))
        self.voltar.clicked.connect(self.abrirprincipal)

        self.confirmar = QtGui.QPushButton(self.centralwidget)
        self.confirmar.setGeometry(QtCore.QRect(510, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.confirmar.setFont(font)
        self.confirmar.setObjectName(_fromUtf8("confirmar"))
        self.confirmar.clicked.connect(self.registraroferta)

        self.lugareslabel = QtGui.QLabel(self.centralwidget)
        self.lugareslabel.setGeometry(QtCore.QRect(40, 400, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(12)
        self.lugareslabel.setFont(font)
        self.lugareslabel.setObjectName(_fromUtf8("lugareslabel"))

        self.lugares = QtGui.QComboBox(self.centralwidget)
        self.lugares.setGeometry(QtCore.QRect(190, 410, 411, 22))
        self.lugares.setEditable(False)
        self.lugares.setObjectName(_fromUtf8("lugares"))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))
        self.lugares.addItem(_fromUtf8(""))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        bairros = sorted(['','Cerqueira César','Vila Leopoldina','Vila Olímpia','Higienópolis','Morumbi','Jardins','Itaim','Jardim Paulista','Moema','Osasco','Itaquera','Alphaville','Pinheiros', 'Alto de Pinheiros', 'Jardim Paulistano', 'Jardim Europa', 'Paraíso','Perdizes','Campo Belo','Consolação','Aclimação','Chácara Inglesa','Chácara Klabin','Butantã'])
        i = 0
        horarios = ['', '0h00','0h30','1h00','1h30','2h00','2h30','3h00','3h30','4h00','4h30','5h00','5h30','6h00','6h30','7h00','7h30','8h00','8h30','9h00','9h30','10h00','10h30','11h00','11h30','12h00','12h30','13h00','13h30','14h00','14h30','15h00','16h00','16h30','17h00','17h30','18h00','18h30','19h00','19h30','20h00','20h30','21h00','21h30','22h00','22h30','23h00','23h30']
        dia = ['','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        mes = ['','1','2','3','4','5','6','7','8','9','10','11','12']

        MainWindow.setWindowTitle(_translate("MainWindow", "Caronas Insper", None))
        for i in range(len(bairros)):
            self.partida.setItemText(i, _translate("MainWindow", bairros[i], None))
            self.destino.setItemText(i, _translate("MainWindow", bairros[i], None))
        for i in range(len(horarios)):
            self.horario.setItemText(i, _translate("MainWindow", horarios[i], None))
        for i in range(len(dia)):
            self.dia.setItemText(i, _translate("MainWindow", dia[i], None))
        for i in range(len(mes)):
            self.mes.setItemText(i, _translate("MainWindow", mes[i], None))
        self.titulo.setText(_translate("MainWindow", "Agende a sua carona:", None))
        self.destinolabel.setText(_translate("MainWindow", "Local de Destino:", None))
        self.partidalabel.setText(_translate("MainWindow", "Local de Partida:", None))
        self.horariolabel.setText(_translate("MainWindow", "Horário:", None))
        self.datalabel.setText(_translate("MainWindow", "Data:", None))
        self.voltar.setText(_translate("MainWindow", "Voltar", None))
        self.confirmar.setText(_translate("MainWindow", "Confirmar", None))
        self.lugares.setItemText(0, _translate("MainWindow", "", None))
        self.lugares.setItemText(1, _translate("MainWindow", "1", None))
        self.lugares.setItemText(2, _translate("MainWindow", "2", None))
        self.lugares.setItemText(3, _translate("MainWindow", "3", None))
        self.lugares.setItemText(4, _translate("MainWindow", "4", None))
        self.lugareslabel.setText(_translate("MainWindow", "Lugares disponíveis:", None))

    def abrirprincipal(self):
        self.MainWindow = principal.Ui_MainWindow
        tela_principal = QtGui.QMainWindow()
        ui = principal.Ui_MainWindow()
        ui.setupUi(tela_principal, self.usuarios, self.nome_completo, self.telefone, self.email)
        tela_principal.show()
        sys.exit(app.exec_())

    def registraroferta(self):
        dlg = QtGui.QMessageBox(None)
        dlg.setWindowTitle("Confirmação")
        dlg.setIcon(QtGui.QMessageBox.Question)
        dlg.setText("Deseja confirmar a oferta?")
        dlg.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        dlg.setDefaultButton(QtGui.QMessageBox.Yes)
        dlg.setEscapeButton(QtGui.QMessageBox.No)
        resultado = dlg.exec_()

        if resultado == QtGui.QMessageBox.Yes:
            fb = firebase.FirebaseApplication('https://caronas.firebaseio.com', None)
            dicionario = {'Horário': self.horario.currentText(), 'Dia':self.dia.currentText(), 'Mês':self.mes.currentText() ,'Local de Partida': self.partida.currentText(), 'Local de Destino': self.destino.currentText(), 'Lugares Necessários': self.lugares.currentText()}
            fb.put('/Ofertas', self.usuarios, dicionario)

            pedidos = fb.get('Pedidos', None)
            
            fb2 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Pedidos/')
            fb3 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Ofertas/')
            fb4 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')


            lugar_saida_oferta = fb3.get(self.usuarios, 'Local de Partida')
            lugar_chegada_oferta = fb3.get(self.usuarios, 'Local de Destino')
            horario_oferta = fb3.get(self.usuarios, 'Horário')
            dia_oferta = fb3.get(self.usuarios, 'Dia')
            mes_oferta = fb3.get(self.usuarios, 'Mês')
            lugares_necessarios_oferta = fb3.get(self.usuarios, 'Lugares Necessários')
            
            for passageiro in pedidos:
                lugar_saida_pedido = fb2.get(passageiro, 'Local de Partida')
                lugar_chegada_pedido = fb2.get(passageiro, 'Local de Destino')
                horario_pedido = fb2.get(passageiro, 'Horário')
                dia_pedido = fb2.get(passageiro, 'Dia')
                mes_pedido = fb2.get(passageiro, 'Mês')
                lugares_necessarios_pedido = fb2.get(passageiro, 'Lugares Necessários')

                lgno = int (lugares_necessarios_oferta) #lugares ofertados transformado em número inteiro
                if lugares_necessarios_pedido != None:
                    lgnp = int (lugares_necessarios_pedido) #lugares pedidos transformado em número inteiro
                else:
                    continue

                if lugar_saida_oferta == lugar_saida_pedido and lugar_chegada_oferta == lugar_chegada_pedido and lugares_necessarios_oferta >= lugares_necessarios_pedido and horario_oferta == horario_pedido and dia_oferta == dia_pedido and mes_oferta == mes_pedido:                    
                    nome = fb4.get(passageiro,'Nome')
                    celular = fb4.get(passageiro, 'telefone')
                    email = fb4.get(passageiro, 'email')
                                        
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = email

                    msg = 'Seu passageiro é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\nData: {3}/{4}\nHorário: {5}\n\nEntre em contato com seu carona para marcarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(nome, celular, email, dia_pedido, mes_pedido, horario_pedido).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = self.email

                    msg = 'Seu motorista é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\nData: {3}/{4}\nHorário: {5}\n\nEntre em contato com seu carona para combinarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(self.nome_completo, self.telefone, self.email, dia_oferta, mes_oferta, horario_oferta).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()

                    lgno -= lgnp
                    
                    fb.delete('/Pedidos', passageiro)

                    if lgno > 0:
                        dicionario['Lugares Necessários'] = lgno
                        fb.put('/Ofertas', self.usuarios, dicionario)
                    
                    dlg = QtGui.QMessageBox(None)
                    dlg.setWindowTitle("Carona")
                    dlg.setIcon(QtGui.QMessageBox.Information)
                    dlg.setText("As informações do seu passageiro estão no seu e-mail!")
                    dlg.exec_()
                    break
            else:
                dlg = QtGui.QMessageBox(None)
                dlg.setWindowTitle("Carona")
                dlg.setIcon(QtGui.QMessageBox.Information)
                dlg.setText("Não existem pedidos de carona no momento. Quando existir alguém, você será notificado por e-mail!")
                dlg.exec_()

            self.MainWindow = principal.Ui_MainWindow
            tela_principal = QtGui.QMainWindow()
            ui = principal.Ui_MainWindow()
            ui.setupUi(tela_principal, self.usuarios, self.nome_completo, self.telefone, self.email)
            tela_principal.show()
            sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, "usuarios", "nome", "tel", "email")
    MainWindow.show()
    sys.exit(app.exec_())

