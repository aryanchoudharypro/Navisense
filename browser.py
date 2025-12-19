from PyQt6.QtCore import QUrl
from process_html import processHTML
import os
from PyQt6.QtWidgets import QMessageBox
def checkLoadStatus(window,is_loaded):
    if not is_loaded:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Unable to load page:")
        msg.setText("the page that you are looking for could not be loaded...")
        msg.setInformativeText("""
        The location that you have entered either doesn't exist or wrong URL/file Path.
        Please recheck and try again...
        Otherwise, contact to file/website owner.
        """)
        msg.setStandardButtons(QMessageBox.standardButton.Ok)
        msg.exec()

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
    webview.page().toHtml(processHTML)

