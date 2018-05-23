import sys
from PyQt4 import QtGui
from winmain import Ui_MainWindow
import os

class Mainwin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Mainwin, self).__init__(parent)
        #QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = Mainwin()
        myapp.show()
        sys.exit(app.exec_())
