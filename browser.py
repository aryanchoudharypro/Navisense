from PyQt6.QtCore import QUrl
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
    processHTML(is_loaded,webview)


def updateAddressBoxURL(address_bar,changed_url):
    address_bar.setText(changed_url.toString())

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

