import caronas, cadastro, login, contato, sobre, principal, pedircarona, agendarcarona, perfil
#from validate_email import validate_email
from PyQt4 import QtCore, QtGui

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    caronas = caronas.Ui_MainWindow()
    caronas.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
