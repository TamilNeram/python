#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("frame_1"))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, _("Some Input"), style=wx.TE_READONLY)
        self.text_ctrl_1.SetBackgroundColour(wx.Colour(0, 255, 127))
        self.text_ctrl_1.SetForegroundColour(wx.Colour(255, 0, 0))
        self.text_ctrl_1.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_ctrl_1.SetFocus()
        sizer_1.Add(self.text_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame_1 = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame_1)
        self.frame_1.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()
