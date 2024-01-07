import sys
from PySide6 import QtCore, QtWidgets, QtGui

sys.path.append("../res")
from GUI import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main_Window()
    sys.exit(app.exec())
