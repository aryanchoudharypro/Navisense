"""
def onLoadHTML(html_code,webview,base_url):
    webview.setHtml(html_code,base_url)
    print(html_code)
"""

def sendToAI(html_code,webview):
    print(html_code)

def processHTML(is_loaded,webview):
    if not is_loaded:
        return
    webview.page().toHtml(lambda html_code: sendToAI(html_code,webview))
