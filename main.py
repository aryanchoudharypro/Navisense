import sys
import os
#os.environ["QT_ACCESSIBILITY"] = "1"
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from toolbar import addressBox
from browser import loadBrowser, updateAddressBoxURL, checkLoadStatus

def startApp():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("NaviSense")
    window.resize(800,600)
    webview = QWebEngineView()
    toolbar, address_bar = (addressBox(lambda url: loadBrowser(url, webview),webview))
    webview.urlChanged.connect(lambda changed_url: updateAddressBoxURL(address_bar,changed_url))
    webview.loadFinished.connect(lambda is_loaded: checkLoadStatus(window,is_loaded,webview))
    window.addToolBar(toolbar)
    window.setCentralWidget(webview)
    welcome_page_path = os.path.abspath("welcome.html")
    webview.load(QUrl.fromLocalFile(welcome_page_path))
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
        startApp()
