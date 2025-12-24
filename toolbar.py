from PyQt6.QtWidgets import QToolBar, QLineEdit, QToolButton, QMenu, QSlider, QLabel, QWidgetAction, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt
from accessibility_features_functions import *

def accessibilityMenue(webview):
    menue = QMenu("Accessibility")
    menue.setWindowTitle("Accessibility Menue")
    menue.setFocus()
    toggal_password_fields = menue.addAction("Toggal password fields")
    toggal_password_fields.setCheckable(True)
    toggal_password_fields.setChecked(False)
    toggal_password_fields.toggled.connect(lambda checked: toggalPasswordFields(checked,webview))
    toggal_dark_mode = menue.addAction("Enable Dark Mode")
    toggal_dark_mode.setCheckable(True)
    toggal_dark_mode.setChecked(False)
    toggal_dark_mode.toggled.connect(lambda checked: toggalDarkMode(checked,webview))
    button = QToolButton()
    button.setText("Accessibility")
    button.setAccessibleName("Accessibility Menue")
    button.setToolTip("Opens accessibility options menu. Press SpaceBar to expand or collapse.")
    button.setAccessibleDescription("Collapse")
    menue.aboutToShow.connect(
        lambda : (
            button.setAccessibleDescription("Expanded"),
            button.setFocus()
        )
    )
    menue.aboutToHide.connect(
        lambda : (
            button.setAccessibleDescription("Collapsed"),
            button. setFocus()
        )
    )
    button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
    button.setMenu(menue)
    return button

def createFontSizeSlider(webview, toolbar):
    font_widjit = QWidget()
    font_size_label = QLabel("Text Size")
    font_layout = QHBoxLayout(font_widjit)
    font_layout.setContentsMargins(6,2,6,2)
    slider_label = QLabel("Text Size")
    slider = QSlider(Qt.Orientation.Horizontal)
    slider.setMinimum(80)
    slider.setMaximum(150)
    slider.setValue(100)
    slider.setSingleStep(5)
    slider.setPageStep(10)
    slider.setAccessibleName("Text Size Slider")
    slider.setAccessibleDescription("Use left and right arrow keys to decrease or increase text size")
    slider.valueChanged.connect(lambda value: setFontSize(value,webview))
    font_layout.addWidget(slider_label)
    font_layout.addWidget(slider)
    slider.setFixedWidth(120)
    slider.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
    slider.valueChanged.connect(lambda value: setFontSize(value,webview))
    toolbar.addWidget(font_size_label)
    toolbar.addWidget(slider)


def addressBox(onclik_url,webview):
    address_bar = QLineEdit()
    address_bar.setPlaceholderText("Address and Sirch bar")
    address_bar.setFocus()
    address_bar.returnPressed.connect(lambda: onclik_url(address_bar.text()))
    toolbar = QToolBar()
    toolbar.addWidget(address_bar)
    toolbar.addWidget(accessibilityMenue(webview))
    createFontSizeSlider(webview,toolbar)
    return toolbar, address_bar
