import caronas, tela_cadastro
from PyQt4 import QtCore, QtGui

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    caronas = caronas.Ui_MainWindow()
    caronas.setupUi(MainWindow)
    MainWindow.show()
    if caronas.self.login.clicked:
	    MainWindow = QtGui.QMainWindow()
	    cadastro = tela_cadastro.Ui_MainWindow()
	    cadastro.setupUi(MainWindow)
	    MainWindow.show()
	    sys.exit(app.exec_())
