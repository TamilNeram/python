#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    May 14, 2021 10:19:10 AM PDT  platform: Linux

import sys

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

import main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("279x145+130+130")
        top.minsize(120, 1)
        top.maxsize(1156, 845)
        top.resizable(0,  0)
        top.title("Main")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(x=58, y=20, height=15, width=162)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(disabledforeground="#b8a786")
        self.Label1.configure(highlightbackground="wheat")
        self.Label1.configure(text='''Progress Bar Example''')

        self.Button1 = tk.Button(top)
        self.Button1.place(x=56, y=55, height=24, width=167)
        self.Button1.configure(activebackground="#ffffcd")
        self.Button1.configure(command=main_support.advance)
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Advance  Progress Bar''')

        self.Button2 = tk.Button(top)
        self.Button2.place(x=116, y=99, height=24, width=47)
        self.Button2.configure(activebackground="#ffffcd")
        self.Button2.configure(command=main_support.quit)
        self.Button2.configure(disabledforeground="#b8a786")
        self.Button2.configure(highlightbackground="wheat")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Quit''')

if __name__ == '__main__':
    vp_start_gui()





