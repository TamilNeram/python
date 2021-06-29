#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.5f
#  in conjunction with Tcl version 8.6
#    Oct 06, 2020 06:03:31 PM PDT  platform: Linux

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

import progress_bar_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    progress_bar_support.set_Tk_var()
    top = Progress_Bar (root)
    progress_bar_support.init(root, top)
    root.mainloop()

w = None
def create_Progress_Bar(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Progress_Bar(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    progress_bar_support.set_Tk_var()
    top = Progress_Bar (w)
    progress_bar_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Progress_Bar():
    global w
    w.destroy()
    w = None

class Progress_Bar:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("203x84+497+139")
        top.minsize(120, 1)
        top.maxsize(1156, 845)
        top.resizable(1,  1)
        top.title("Progress Bar")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.099, rely=0.357, relwidth=0.788
                , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="160")
        self.TProgressbar1.configure(variable=progress_bar_support.prog_var)

if __name__ == '__main__':
    vp_start_gui()





