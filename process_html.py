from openai import OpenAI
def sendToAI(html_code,webview):
    client = OpenAI()
    prompt = f"""
You are an accessibility expert.
Analyze the HTML below and return ONLY JavaScript code that improves accessibility on the LIVE page using dom Manipulation.
Rules:
- Return ONLY JavaScript (no explanation, no markdown)
- Do NOT reload the page
- Do NOT use document.write
- Use DOM manipulation only
- Add missing labels, aria-labels, roles
- Fix unlabeled buttons and inputs
-add required landmarks
- Do NOT change visible text meaning
html:
{html_code}
"""
    response = client.responses.create(
        model="gpt-4.1-mini",
        input = prompt
    )
    js_code = response.output_text
    webview.page().runJavaScript(js_code)

def processHTML(is_loaded,webview):
    if not is_loaded:
        return
    webview.page().toHtml(lambda html_code: sendToAI(html_code,webview))

