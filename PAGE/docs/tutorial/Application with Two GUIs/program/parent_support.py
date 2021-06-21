#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     parent_support.py
#  ------------------------------------------------------
# Created for Full Circle Magazine #155
# Written by G.D. Walters
# Copyright (c) 2020 by G.D. Walters
# This source code is released under the MIT License
# ======================================================

# Support module generated by PAGE version 5.0.2c
#  in conjunction with Tcl version 8.6
#    Feb 20, 2020 11:37:13 AM CST  platform: Linux

import sys
import child
import child_support
import shared

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def set_Tk_var():
    global StatusLabel
    StatusLabel = tk.StringVar()
    StatusLabel.set('')
    global DataReceived
    DataReceived = tk.StringVar()
    DataReceived.set('')


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    # ======================================================
    # My init code starts...
    # ======================================================
    shared.child_active = False
    shared.ReadyToRead = False
    global LblStat
    LblStat = w.Label5
    LblStat.configure(background='RED')
    global comm1
    comm1 = root.after(0, on_tick)


def on_tick():
    global comm1
    global LblStat
    # print('on_tick')
    if shared.child_active == True:
        LblStat.configure(background='GREEN')
        if shared.ReadyToRead:
            DataReceived.set(shared.ChildData)
            shared.ReadyToRead = False
    elif shared.child_active == False:
        LblStat.configure(background='RED')

    comm1 = root.after(100, on_tick)


def on_btnExit():
    # print('parent_support.on_btnExit')
    # sys.stdout.flush()
    destroy_window()


def on_btnLaunch():
    # print('parent_support.on_btnLaunch')
    # sys.stdout.flush()
    child.create_Toplevel1(root)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import parent
    parent.vp_start_gui()