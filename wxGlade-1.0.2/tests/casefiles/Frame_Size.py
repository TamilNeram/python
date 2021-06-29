#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx




class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("frame")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_1.Add(self.text_ctrl_1, 0, 0, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "button_1")
        sizer_1.Add(self.button_1, 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle("frame")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_1.Add(self.text_ctrl_1, 0, 0, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "button_1")
        sizer_1.Add(self.button_1, 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        sizer_1.Fit(self)
        self.Layout()


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
