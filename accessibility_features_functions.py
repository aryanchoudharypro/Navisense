def toggalPasswordFields(checked, webview):
    js = """
    document.querySelectorAll("input").forEach(input => {

        // Mark original password fields once
        if (input.type === "password" && !input.dataset.originalType) {
            input.dataset.originalType = "password";
        }

        // Toggle logic
        if (input.dataset.originalType === "password") {
            input.type = %s;
        }
    });
    """ % ("'text'" if checked else "'password'")
    webview.page().runJavaScript(js)

def toggalDarkMode(checked, webview):
    js = """
        (function () {
        let style = document.getElementById("navisense-dark-mode");

        if (%s) {
            if (!style) {
                style = document.createElement("style");
                style.id = "navisense-dark-mode";
                style.innerHTML = `
                    html, body {
                        background-color: #121212 !important;
                        color: #e0e0e0 !important;
                    }

                    * {
                        background-color: transparent !important;
                        color: inherit !important;
                        border-color: #555 !important;
                    }

                    a {
                        color: #8ab4f8 !important;
                    }

                    input, textarea, select, button {
                        background-color: #1e1e1e !important;
                        color: #ffffff !important;
                    }
                `;
                document.head.appendChild(style);
            }
        } else {
            if (style) {
                style.remove();
            }
        }
    })();
    """ % ("true" if checked else "false")
    webview.page().runJavaScript(js)


def setFontSize(percent, webview):
    js = f"""
    (function() {{
        document.documentElement.style.fontSize = '{percent}%';
    }})();
"""
    webview.page().runJavaScript(js)