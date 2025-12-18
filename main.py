import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from toolbar import addressBox
from browser import loadBrowser

def startApp():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("NaviSense")
    window.resize(800,600)
    window.addToolBar(addressBox(loadBrowser))
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
        startApp()
