import wx
from accessibility_features_functions import *

def accessibilityMenue(parent, webview):
    menue = wx.Menu()
    toggal_password_fields = menue.AppendCheckItem(wx.ID_ANY, "Toggal password fields")
    menue.Bind(
        wx.EVT_MENU,
        lambda event: toggalPasswordFields(toggal_password_fields.IsChecked(), webview),
        toggal_password_fields,
    )
    toggal_dark_mode = menue.AppendCheckItem(wx.ID_ANY, "Enable Dark Mode")
    menue.Bind(
        wx.EVT_MENU,
        lambda event: toggalDarkMode(toggal_dark_mode.IsChecked(), webview),
        toggal_dark_mode,
    )

    button = wx.Button(parent, label="Accessibility")
    button.SetName("Accessibility Menue")
    button.SetToolTip("Opens accessibility options menu. Press SpaceBar to expand or collapse.")
    button.SetHelpText("Collapse")

    def onClick(event):
        button.SetHelpText("Expanded")
        button.PopupMenu(menue, 0, button.GetSize().height)
        button.SetHelpText("Collapsed")
        button.SetFocus()

    button.Bind(wx.EVT_BUTTON, onClick)
    return button

def createFontSizeSlider(toolbar, webview):
    font_widjit = wx.Panel(toolbar)
    font_layout = wx.BoxSizer(wx.HORIZONTAL)
    slider_label = wx.StaticText(font_widjit, label="Text Size")
    slider = wx.Slider(
        font_widjit,
        value=100,
        minValue=80,
        maxValue=150,
        size=(120, -1),
        style=wx.SL_HORIZONTAL,
    )
    slider.SetName("Text Size Slider")
    slider.SetToolTip("Use left and right arrow keys to decrease or increase text size")
    slider.SetLineSize(5)
    slider.SetPageSize(10)
    slider.Bind(wx.EVT_SLIDER, lambda event: setFontSize(slider.GetValue(), webview))
    font_layout.Add(slider_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 6)
    font_layout.Add(slider, 0, wx.ALIGN_CENTER_VERTICAL)
    font_widjit.SetSizerAndFit(font_layout)
    toolbar.AddControl(font_widjit)


def addressBox(frame, onclik_url, webview):
    toolbar = wx.ToolBar(frame, style=wx.TB_HORIZONTAL)
    address_bar = wx.TextCtrl(toolbar, style=wx.TE_PROCESS_ENTER, size=(400, -1))
    address_bar.SetHint("Address and Sirch bar")
    address_bar.SetName("Address and Sirch bar")
    address_bar.Bind(wx.EVT_TEXT_ENTER, lambda event: onclik_url(address_bar.GetValue()))
    toolbar.AddControl(address_bar)
    toolbar.AddControl(accessibilityMenue(toolbar, webview))
    createFontSizeSlider(toolbar, webview)
    toolbar.Realize()
    address_bar.SetFocus()
    return toolbar, address_bar
