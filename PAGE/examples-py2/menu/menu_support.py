#! /usr/bin/env python
#
# Support module generated by PAGE version 4.10a7
# In conjunction with Tcl version 8.6
#    Jan 06, 2018 09:32:44 PM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    global IRS
    IRS = StringVar()
    global Charity
    Charity = StringVar()
    global Check_1
    Check_1 = StringVar()
    global Check_2
    Check_2 = StringVar()

def check1():
    print('menu_support.check1')
    sys.stdout.flush()

def check2():
    print('menu_support.check2')
    sys.stdout.flush()

def copy():
    print('menu_support.copy')
    sys.stdout.flush()

def cut():
    print('menu_support.cut')
    sys.stdout.flush()

def no():
    print('menu_support.no')
    sys.stdout.flush()

def paste():
    print('menu_support.paste')
    sys.stdout.flush()

def post():
    print('menu_support.post')
    sys.stdout.flush()

def quit():
    print('menu_support.quit')
    sys.stdout.flush()
    sys.exit()

def radio_a():
    print('menu_support.radio_a')
    sys.stdout.flush()

def radio_b():
    print('menu_support.radio_b')
    sys.stdout.flush()

def save():
    print('menu_support.save')
    sys.stdout.flush()

def sync():
    print('menu_support.sync')
    sys.stdout.flush()

def yes():
    print('menu_support.yes')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import menu
    menu.vp_start_gui()




