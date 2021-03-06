# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.9pre on Wed Apr  1 22:51:19 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import wx.py.shell
# end wxGlade


class ShellFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ShellFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((800, 668))
        self.SetTitle("wxGlade Shell ")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("icons/wxglade128.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        
        self.panel = wx.Panel(self, wx.ID_ANY)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        grid_sizer = wx.FlexGridSizer(1, 3, 0, 0)
        sizer.Add(grid_sizer, 0, wx.EXPAND, 0)
        
        label = wx.StaticText(self.panel, wx.ID_ANY, "Path:")
        grid_sizer.Add(label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        
        self.txt_path = wx.TextCtrl(self.panel, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer.Add(self.txt_path, 0, wx.EXPAND, 0)
        
        self.btn_assign = wx.Button(self.panel, wx.ID_ANY, "Assign to variable")
        grid_sizer.Add(self.btn_assign, 0, 0, 0)
        
        self.shell = wx.py.shell.Shell(self.panel, wx.ID_ANY, introText = "\nThis is the shell.\nModules 'common' and 'misc' are imported already.\n\n")
        # insert some variables into the shell's locals
        import common, misc
        self.shell.interp.locals["common"] = common
        self.shell.interp.locals["misc"] = misc
        
        sizer.Add(self.shell, 2, wx.EXPAND, 0)
        
        grid_sizer.AddGrowableCol(1)
        
        self.panel.SetSizer(sizer)
        
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.on_btn_assign, self.btn_assign)
        # end wxGlade

    def on_btn_assign(self, event):  # wxGlade: ShellFrame.<event_handler>
        print("Event handler 'on_btn_assign' not implemented!")
        event.Skip()
# end of class ShellFrame
