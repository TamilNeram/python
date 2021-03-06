#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0a9 on Sun Nov 19 22:21:27 2017
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import wx.py.shell
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((800, 379))
        self.SetTitle("frame")
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        
        self.text_ctrl = wx.TextCtrl(self.panel_1, wx.ID_ANY, "This is text_ctrl.\n\nUse the shell to append text here.\nE.g. enter this:\napp.frame.text_ctrl.AppendText(\"line of text\\n\")\n", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.text_ctrl.SetMinSize((200, 10))
        self.text_ctrl.SetBackgroundColour(wx.Colour(192, 192, 192))
        sizer_2.Add(self.text_ctrl, 1, wx.ALL | wx.EXPAND, 1)
        
        self.shell = wx.py.shell.Shell(self.panel_1, wx.ID_ANY, introText = "\nThis is the shell.\nHave a look at the variables 'app' and 'app.frame'.\n\n")
        sizer_2.Add(self.shell, 2, wx.EXPAND, 0)
        
        self.panel_1.SetSizer(sizer_2)
        
        self.SetSizer(sizer_1)
        
        self.Layout()
        # end wxGlade

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
