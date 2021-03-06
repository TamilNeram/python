#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0a9 on Mon Dec  4 21:53:58 2017
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import wx.html2
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((800, 600))
        self.SetTitle("html2 example")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)

        self.button_back = wx.Button(self.panel_1, wx.ID_ANY, "<--")
        self.button_back.SetMinSize((30, -1))
        sizer_3.Add(self.button_back, 0, 0, 0)

        self.button_forward = wx.Button(self.panel_1, wx.ID_ANY, "-->")
        self.button_forward.SetMinSize((30, -1))
        sizer_3.Add(self.button_forward, 0, 0, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Location:")
        sizer_3.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)

        self.text_url = wx.TextCtrl(self.panel_1, wx.ID_ANY, "http://www.python.org/")
        sizer_3.Add(self.text_url, 1, 0, 0)

        self.button_go = wx.Button(self.panel_1, wx.ID_ANY, "Open")
        self.button_go.SetDefault()
        sizer_3.Add(self.button_go, 0, 0, 0)

        self.html2 = wx.html2.WebView.New(self.panel_1)
        sizer_2.Add(self.html2, 1, wx.ALL | wx.EXPAND, 3)

        self.panel_1.SetSizer(sizer_2)

        self.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, lambda event: self.html2.CanGoBack() and self.html2.GoBack(), self.button_back)
        self.Bind(wx.EVT_BUTTON, lambda event: self.html2.CanGoForward() and self.html2.GoForward(), self.button_forward)
        self.Bind(wx.EVT_BUTTON, lambda event:self.html2.LoadURL( self.text_url.GetValue() ), self.button_go)
        self.Bind(wx.html2.EVT_WEBVIEW_ERROR, self.on_webview_error, self.html2)
        self.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.on_webview_loaded, self.html2)
        self.Bind(wx.html2.EVT_WEBVIEW_NAVIGATED, self.on_webview_navigated, self.html2)
        self.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.on_webview_navigating, self.html2)
        self.Bind(wx.html2.EVT_WEBVIEW_NEWWINDOW, self.on_webview_newwindow, self.html2)
        self.Bind(wx.html2.EVT_WEBVIEW_TITLE_CHANGED, self.on_webview_title_changed, self.html2)
        # end wxGlade

    def on_webview_error(self, event):  # wxGlade: MyFrame.<event_handler>
        print("EVT_WEBVIEW_ERROR", event.GetString())
        event.Skip()

    def on_webview_loaded(self, event):  # wxGlade: MyFrame.<event_handler>
        print("EVT_WEBVIEW_LOADED", event.GetURL())
        event.Skip()

    def on_webview_navigated(self, event):  # wxGlade: MyFrame.<event_handler>
        print("EVT_WEBVIEW_NAVIGATED", event.GetNavigationAction(), event.GetTarget(), event.GetURL())
        event.Skip()

    def on_webview_navigating(self, event):  # wxGlade: MyFrame.<event_handler>
        print("EVT_WEBVIEW_NAVIGATING", event.GetNavigationAction(), event.GetTarget(), event.GetURL())
        # call event.Veto() to veto
        event.Skip()

    def on_webview_newwindow(self, event):  # wxGlade: MyFrame.<event_handler>
        print("EVT_WEBVIEW_NEWWINDOW", event.GetURL())
        event.Skip()

    def on_webview_title_changed(self, event):  # wxGlade: MyFrame.<event_handler>
        print("EVT_WEBVIEW_TITLE_CHANGED", event.GetString())
        event.Skip()
# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
