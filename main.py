import os
import wx
import wx.html2 as html2
from toolbar import addressBox
from browser import loadBrowser, updateAddressBoxURL, checkLoadStatus

class NavisenseFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="NaviSense", size=(800, 600))

        self.webview = html2.WebView.New(self)
        self.webview.SetName("Web content")

        self.toolbar, self.address_bar = addressBox(
            self, lambda url: loadBrowser(url, self.webview), self.webview
        )
        self.SetToolBar(self.toolbar)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.webview, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.webview.Bind(html2.EVT_WEBVIEW_NAVIGATED, self.onURLChanged)
        self.webview.Bind(html2.EVT_WEBVIEW_LOADED, self.onLoadFinished)
        self.webview.Bind(html2.EVT_WEBVIEW_ERROR, self.onLoadError)

        welcome_page_path = os.path.abspath("welcome.html")
        loadBrowser(welcome_page_path, self.webview)

    def onURLChanged(self, event):
        updateAddressBoxURL(self.address_bar, event.GetURL())

    def onLoadFinished(self, event):
        checkLoadStatus(self, True, self.webview)

    def onLoadError(self, event):
        checkLoadStatus(self, False, self.webview)

def startApp():
    app = wx.App()
    window = NavisenseFrame()
    window.Show()
    app.MainLoop()

if __name__ == "__main__":
        startApp()
