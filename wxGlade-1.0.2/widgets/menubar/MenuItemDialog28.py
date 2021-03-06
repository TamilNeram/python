# -*- coding: CP1252 -*-
#
# generated by wxGlade 1.0.0a8 on Sun Oct  4 20:07:03 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MenuItemDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MenuItemDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((900, 600))
        self.SetTitle("Menu Editor")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_5, 0, wx.EXPAND, 0)

        grid_sizer_2 = wx.FlexGridSizer(5, 2, 0, 0)
        sizer_5.Add(grid_sizer_2, 2, wx.EXPAND, 0)

        label_6 = wx.StaticText(self, wx.ID_ANY, "Label:")
        label_6.SetToolTipString("The menu entry text;\nenter & for access keys (using ALT key)\nappend e.g. \\tCtrl-X for keyboard shortcut")
        grid_sizer_2.Add(label_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.label = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label.SetToolTipString("The menu entry text;\nenter & for access keys (using ALT key)\nappend e.g. \\tCtrl-X for keyboard shortcut")
        grid_sizer_2.Add(self.label, 1, wx.EXPAND, 0)

        label_7 = wx.StaticText(self, wx.ID_ANY, "Event Handler:")
        label_7.SetToolTipString("Enter the name of an event handler method; this will be created as stub.\n\nAlternatively, for Python you may supply a lambda function like e.g.:\nlambda evt: self.on_menu_item('item x')")
        grid_sizer_2.Add(label_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.event_handler = wx.TextCtrl(self, wx.ID_ANY, "")
        self.event_handler.SetToolTipString("Enter the name of an event handler method; this will be created as stub.\n\nAlternatively, for Python you may supply a lambda function like e.g.:\nlambda evt: self.on_menu_item('item x')")
        grid_sizer_2.Add(self.event_handler, 1, wx.EXPAND, 0)

        label_8 = wx.StaticText(self, wx.ID_ANY, "(Attribute) Name:")
        label_8.SetToolTipString("optional: enter a name to store the menu item as attribute of the menu bar")
        grid_sizer_2.Add(label_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.name = wx.TextCtrl(self, wx.ID_ANY, "")
        self.name.SetToolTipString("optional: enter a name to store the menu item as attribute of the menu bar")
        grid_sizer_2.Add(self.name, 1, wx.EXPAND, 0)

        label_9 = wx.StaticText(self, wx.ID_ANY, "Help String:")
        grid_sizer_2.Add(label_9, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.help_str = wx.TextCtrl(self, wx.ID_ANY, "")
        grid_sizer_2.Add(self.help_str, 1, wx.EXPAND, 0)

        label_10 = wx.StaticText(self, wx.ID_ANY, "ID:")
        label_10.SetToolTipString("optional: enter wx ID")
        grid_sizer_2.Add(label_10, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)

        self.id = wx.TextCtrl(self, wx.ID_ANY, "")
        self.id.SetToolTipString("optional: enter wx ID")
        grid_sizer_2.Add(self.id, 0, 0, 0)

        self.type = wx.RadioBox(self, wx.ID_ANY, "Type", choices=["Normal", "Checkable", "Radio"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.type.SetSelection(0)
        sizer_5.Add(self.type, 0, wx.ALL | wx.EXPAND, 4)

        sizer_5.Add((20, 20), 1, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_6, 0, wx.EXPAND, 0)

        self.ok = wx.Button(self, wx.ID_OK, "&OK")
        self.ok.SetToolTipString("Alt+O or Alt+Enter or Ctrl+Enter")
        sizer_6.Add(self.ok, 0, wx.ALL, 5)

        self.cancel = wx.Button(self, wx.ID_CANCEL, "&Cancel")
        self.cancel.SetToolTipString("Alt+C or Alt+F4")
        sizer_6.Add(self.cancel, 0, wx.ALL, 5)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)

        self.move_left = wx.Button(self, wx.ID_ANY, "&<")
        self.move_left.SetToolTipString("Move the selected item up by one menu level (Alt-Left)")
        sizer_2.Add(self.move_left, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 8)

        self.move_right = wx.Button(self, wx.ID_ANY, "&>")
        self.move_right.SetToolTipString("Move the selected item down by one menu level (Alt-Right)")
        sizer_2.Add(self.move_right, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 8)

        self.move_up = wx.Button(self, wx.ID_ANY, "&Up")
        self.move_up.SetToolTipString("Move selected item up (Alt-Up)")
        sizer_2.Add(self.move_up, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 8)

        self.move_down = wx.Button(self, wx.ID_ANY, "&Down")
        self.move_down.SetToolTipString("Move selected item down (Alt-Down)")
        sizer_2.Add(self.move_down, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 8)

        sizer_2.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL, 0)

        self.add = wx.Button(self, wx.ID_ANY, "&Add")
        self.add.SetToolTipString("Alt+A")
        sizer_2.Add(self.add, 0, wx.BOTTOM | wx.LEFT | wx.TOP, 8)

        self.remove = wx.Button(self, wx.ID_ANY, "&Remove")
        self.remove.SetToolTipString("Alt+R")
        sizer_2.Add(self.remove, 0, wx.BOTTOM | wx.TOP, 8)

        self.add_sep = wx.Button(self, wx.ID_ANY, "Add &Separator")
        self.add_sep.SetToolTipString("Alt+S")
        sizer_2.Add(self.add_sep, 0, wx.ALL, 8)

        sizer_2.Add((20, 20), 2, wx.ALIGN_CENTER_VERTICAL, 0)

        self.items = wx.ListCtrl(self, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_EDIT_LABELS | wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.items.SetToolTipString("For navigation use the mouse or the up/down arrows")
        self.items.InsertColumn(0, "Level", format=wx.LIST_FORMAT_LEFT, width=30)
        self.items.InsertColumn(1, "Label", format=wx.LIST_FORMAT_LEFT, width=180)
        self.items.InsertColumn(2, "Event Handler", format=wx.LIST_FORMAT_LEFT, width=180)
        self.items.InsertColumn(3, "Name", format=wx.LIST_FORMAT_LEFT, width=120)
        self.items.InsertColumn(4, "Type", format=wx.LIST_FORMAT_LEFT, width=35)
        self.items.InsertColumn(5, "Help String", format=wx.LIST_FORMAT_LEFT, width=250)
        self.items.InsertColumn(6, "ID", format=wx.LIST_FORMAT_LEFT, width=50)
        sizer_1.Add(self.items, 1, wx.EXPAND, 0)

        grid_sizer_2.AddGrowableCol(1)

        self.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_TEXT, self.on_label_edited, self.label)
        self.Bind(wx.EVT_TEXT, self.on_event_handler_edited, self.event_handler)
        self.Bind(wx.EVT_TEXT, self.on_name_edited, self.name)
        self.Bind(wx.EVT_TEXT, self.on_help_str_edited, self.help_str)
        self.Bind(wx.EVT_TEXT, self.on_id_edited, self.id)
        self.Bind(wx.EVT_RADIOBOX, self.on_type_edited, self.type)
        self.Bind(wx.EVT_BUTTON, self.on_OK, self.ok)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, self.cancel)
        self.Bind(wx.EVT_BUTTON, self.move_item_left, self.move_left)
        self.Bind(wx.EVT_BUTTON, self.move_item_right, self.move_right)
        self.Bind(wx.EVT_BUTTON, self.move_item_up, self.move_up)
        self.Bind(wx.EVT_BUTTON, self.move_item_down, self.move_down)
        self.Bind(wx.EVT_BUTTON, self.add_item, self.add)
        self.Bind(wx.EVT_BUTTON, self.remove_item, self.remove)
        self.Bind(wx.EVT_BUTTON, self.add_separator, self.add_sep)
        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.on_label_edited, self.items)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.show_item, self.items)
        # end wxGlade

    def on_label_edited(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'on_label_edited' not implemented!")
        event.Skip()

    def on_event_handler_edited(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'on_event_handler_edited' not implemented!")
        event.Skip()

    def on_name_edited(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'on_name_edited' not implemented!")
        event.Skip()

    def on_help_str_edited(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'on_help_str_edited' not implemented!")
        event.Skip()

    def on_id_edited(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'on_id_edited' not implemented!")
        event.Skip()

    def on_type_edited(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'on_type_edited' not implemented!")
        event.Skip()

    def on_OK(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'on_OK' not implemented!")
        event.Skip()

    def on_cancel(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'on_cancel' not implemented!")
        event.Skip()

    def move_item_left(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'move_item_left' not implemented!")
        event.Skip()

    def move_item_right(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'move_item_right' not implemented!")
        event.Skip()

    def move_item_up(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'move_item_up' not implemented!")
        event.Skip()

    def move_item_down(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'move_item_down' not implemented!")
        event.Skip()

    def add_item(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'add_item' not implemented!")
        event.Skip()

    def remove_item(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'remove_item' not implemented!")
        event.Skip()

    def add_separator(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'add_separator' not implemented!")
        event.Skip()

    def show_item(self, event):  # wxGlade: MenuItemDialog.<event_handler>
        print("Event handler 'show_item' not implemented!")
        event.Skip()

# end of class MenuItemDialog
