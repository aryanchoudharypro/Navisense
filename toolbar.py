from PyQt6.QtWidgets import QToolBar, QLineEdit
def addressBox(onclik_url):
    address_bar = QLineEdit()
    address_bar.setPlaceholderText("Address and Sirch bar")
    address_bar.returnPressed.connect(lambda: onclik_url(address_bar.text()))
    toolbar = QToolBar()
    toolbar.addWidget(address_bar)

    return toolbar
