# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.6 on Mon Jul 20 23:46:03 2020
#

import wx
import wx.grid

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import my_grid
# end wxGlade


class TestGlade(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: TestGlade.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.grid = my_grid.MyGrid(self, wx.ID_ANY, size=(1, 1))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: TestGlade.__set_properties
        self.grid.CreateGrid(0, 1)
        self.grid.SetRowLabelSize(0)
        self.grid.SetColLabelSize(0)
        self.grid.EnableEditing(0)
        self.grid.EnableGridLines(0)
        self.grid.EnableDragColSize(0)
        self.grid.EnableDragRowSize(0)
        self.grid.SetColLabelValue(0, "")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: TestGlade.__do_layout
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.grid, 1, wx.EXPAND, 0)
        self.SetSizer(main_sizer)
        main_sizer.Fit(self)
        self.Layout()
        # end wxGlade

# end of class TestGlade
