# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contato.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import smtplib, caronas
from validate_email import validate_email

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
        self.oprojetolabel.setGeometry(QtCore.QRect(340, 50, 161, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.oprojetolabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(36)
        font.setUnderline(False)
        self.oprojetolabel.setFont(font)
        self.oprojetolabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.oprojetolabel.setObjectName(_fromUtf8("oprojetolabel"))



        self.voltar = QtGui.QPushButton(self.centralwidget)
        self.voltar.setGeometry(QtCore.QRect(100, 460, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.voltar.setFont(font)
        self.voltar.setObjectName(_fromUtf8("voltar"))
        self.voltar.clicked.connect(self.abrircaronas)



        self.contato = QtGui.QPlainTextEdit(self.centralwidget)
        self.contato.setGeometry(QtCore.QRect(100, 150, 641, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        self.contato.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.contato.setFont(font)
        self.contato.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.contato.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.contato.setLineWrapMode(QtGui.QPlainTextEdit.WidgetWidth)
        self.contato.setReadOnly(True)
        self.contato.setTabStopWidth(80)
        self.contato.setCenterOnScroll(False)
        self.contato.setObjectName(_fromUtf8("contato"))


        self.emailinput = QtGui.QLabel(self.centralwidget)
        self.emailinput.setGeometry(QtCore.QRect(100, 270, 181, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.emailinput.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(16)
        self.emailinput.setFont(font)
        self.emailinput.setObjectName(_fromUtf8("emailinput"))


        self.mensagemlabel = QtGui.QLabel(self.centralwidget)
        self.mensagemlabel.setGeometry(QtCore.QRect(100, 310, 181, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.mensagemlabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bodoni MT"))
        font.setPointSize(16)
        self.mensagemlabel.setFont(font)
        self.mensagemlabel.setObjectName(_fromUtf8("mensagemlabel"))


        self.mensagem = QtGui.QTextEdit(self.centralwidget)
        self.mensagem.setGeometry(QtCore.QRect(100, 350, 641, 101))
        self.mensagem.setObjectName(_fromUtf8("mensagem"))

        self.enviar = QtGui.QPushButton(self.centralwidget)
        self.enviar.setGeometry(QtCore.QRect(640, 460, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(8)
        self.enviar.setFont(font)
        self.enviar.setObjectName(_fromUtf8("enviar"))
        self.enviar.clicked.connect(self.enviarmensagem)


        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 280, 531, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Caronas Insper", None))
        self.oprojetolabel.setText(_translate("MainWindow", "Contato", None))
        self.voltar.setText(_translate("MainWindow", "Voltar", None))
        self.contato.setPlainText(_translate("MainWindow", "Tem alguma dúvida, sugestão ou reclamação para desenvolvermos um aplicativo melhor?\n"
"\n"
"Mande-nos um e-mail que lhe retornaremos o mais rápido possível!", None))
        self.emailinput.setText(_translate("MainWindow", "Seu e-mail:", None))
        self.mensagemlabel.setText(_translate("MainWindow", "Mensagem:", None))
        self.enviar.setText(_translate("MainWindow", "Enviar", None))

    def abrircaronas(self):
        self.MainWindow = caronas.Ui_MainWindow
        tela_caronas = QtGui.QMainWindow()
        ui = caronas.Ui_MainWindow()
        ui.setupUi(tela_caronas)
        tela_caronas.show()
        sys.exit(app.exec_())

    def enviarmensagem(self):
        validando_email = validate_email(self.lineEdit.text())
        if validando_email == True:
            fromaddr = self.lineEdit.text()
            toaddrs = 'lucarn@al.insper.edu.br'

            msg = self.mensagem.toPlainText()
                        
            server = smtplib.SMTP('insper.edu.br')
            server.set_debuglevel(1)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()

            dlg = QtGui.QMessageBox(None)
            dlg.setWindowTitle("Contato")
            dlg.setIcon(QtGui.QMessageBox.Information)
            dlg.setText("Mensagem enviada com sucesso!")
            dlg.exec_()
        else:
            dlg = QtGui.QMessageBox(None)
            dlg.setWindowTitle("Contato")
            dlg.setIcon(QtGui.QMessageBox.Information)
            dlg.setText("Não foi possível enviar sua mensagem. Verifique seu e-mail.")
            dlg.exec_()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

