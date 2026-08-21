import os
import wx
from process_html import processHTML


def checkLoadStatus(window, is_loaded, webview):
    if not is_loaded:
        wx.MessageBox(
            "Sorry, the page could not be loaded... Please recheck the location and try again.",
            "Enable to load page",
            wx.OK | wx.ICON_ERROR,
            window,
        )
        return
    webview.SetFocus()
    processHTML(is_loaded, webview)


def updateAddressBoxURL(address_bar, changed_url):
    address_bar.SetValue(changed_url)
    if "welcome.html" in changed_url:
        address_bar.Clear()


def loadBrowser(url, webview):
    url = url.lower()
    url = url.strip()
    if url.startswith("file://"):
        pass
    elif os.path.exists(url):
        url = "file://" + os.path.abspath(url)
    else:
        if not url.startswith("http"):
            url = "http://" + url
    webview.LoadURL(url)
