#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    May 14, 2021 09:06:45 AM PDT  platform: Linux

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

import standard_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    standard_support.set_Tk_var()
    top = Toplevel1 (root)
    standard_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    standard_support.set_Tk_var()
    top = Toplevel1 (w)
    standard_support.init(w, top, *args, **kwargs)
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x369+276+138")
        top.minsize(120, 1)
        top.maxsize(1156, 845)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.033, rely=0.051, height=25, width=76)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Tbutton''')

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TCheckbutton1 = ttk.Checkbutton(top)
        self.TCheckbutton1.place(relx=0.217, rely=0.051, relwidth=0.113
                , relheight=0.0, height=20)
        self.TCheckbutton1.configure(variable=standard_support.tch46)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Tcheck''')

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.383, rely=0.051, relheight=0.054
                , relwidth=0.238)
        self.TCombobox1.configure(textvariable=standard_support.combobox)
        self.TCombobox1.configure(takefocus="")

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.733, rely=0.051, relheight=0.054
                , relwidth=0.21)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="xterm")

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.05, rely=0.157, relheight=0.195
                , relwidth=0.208)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.367, rely=0.157, height=18, width=46)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Tlabel''')

        self.TLabelframe1 = ttk.Labelframe(top)
        self.TLabelframe1.place(relx=0.567, rely=0.157, relheight=0.195
                , relwidth=0.25)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''Tlabelframe''')

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.033, rely=0.444, relheight=0.431
                , relwidth=0.34)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Page 1",compound="left",underline="-1",)
        self.TNotebook1_t1.configure(highlightbackground="wheat")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="Page 2",compound="left",underline="-1",)
        self.TNotebook1_t2.configure(highlightbackground="wheat")

        self.TPanedwindow1 = ttk.Panedwindow(top, orient="horizontal")
        self.TPanedwindow1.place(relx=0.467, rely=0.366, relheight=0.339
                , relwidth=0.342)
        self.TPanedwindow1_p1 = ttk.Labelframe(self.TPanedwindow1, width=75
                , text='Pane 1')
        self.TPanedwindow1.add(self.TPanedwindow1_p1, weight=0)
        self.TPanedwindow1_p2 = ttk.Labelframe(self.TPanedwindow1, text='Pane 2')

        self.TPanedwindow1.add(self.TPanedwindow1_p2, weight=0)
        self.__funcid0 = self.TPanedwindow1.bind('<Map>', self.__adjust_sash0)

        self.style.configure('TSizegrip', background=_bgcolor)
        self.TSizegrip1 = ttk.Sizegrip(top)
        self.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.417, rely=0.39,  relheight=0.444)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.45, rely=0.832,  relwidth=0.333)

    def __adjust_sash0(self, event):
        paned = event.widget
        pos = [75, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid0)
        del self.__funcid0

if __name__ == '__main__':
    vp_start_gui()





