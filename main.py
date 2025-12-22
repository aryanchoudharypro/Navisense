import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from toolbar import addressBox
from browser import loadBrowser, updateAddressBoxURL, checkLoadStatus

def startApp():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("NaviSense")
    window.resize(800,600)
    webview = QWebEngineView()
    toolbar, address_bar = (addressBox(lambda url: loadBrowser(url, webview)))
    webview.urlChanged.connect(lambda changed_url: updateAddressBoxURL(address_bar,changed_url))
    webview.loadFinished.connect(lambda is_loaded: checkLoadStatus(window,is_loaded,webview))
    window.addToolBar(toolbar)
    window.setCentralWidget(webview)
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
        startApp()
