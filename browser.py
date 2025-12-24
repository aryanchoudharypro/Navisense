from PyQt6.QtCore import QUrl, Qt
from process_html import processHTML
import os
from PyQt6.QtWidgets import QMessageBox
def checkLoadStatus(window,is_loaded,webview):
    if not is_loaded:
        QMessageBox.critical(
            window,
            "Enable to load page",
            "Sorry, the page could not be loaded... Please recheck the location and try again.",
        )
        return
    webview.setFocus()
    webview.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
    processHTML(is_loaded,webview)


def updateAddressBoxURL(address_bar,changed_url):
    address_bar.setText(changed_url.toString())
    if "welcome.html" in changed_url.toString():
        address_bar.clear()


def loadBrowser(url,webview):
    url = url.lower()
    url = url.strip()
    if url.startswith("file://"):
        url = QUrl(url)
    elif os.path.exists(url):
        url = QUrl.fromLocalFile(os.path.abspath(url))
    else:
        if not url.startswith("http"):
            url = "http://" + url
    webview.load(QUrl(url))

