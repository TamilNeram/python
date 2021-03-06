#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.8.7a
# In conjunction with Tcl version 8.6
#    Jan 16, 2017 06:49:58 PM
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

import main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Main (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Main(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Main (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Main():
    global w
    w.destroy()
    w = None


class Main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}' 
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2' 
        font10 = "-family {DejaVu Sans} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"

        top.geometry("600x450+650+150")
        top.title("Main")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")



        self.Button1 = Button(top)
        self.Button1.place(relx=0.4, rely=0.36, height=35, width=118)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(background="wheat")
        self.Button1.configure(command=main_support.open_two)
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(font=font10)
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(text='''Make Two''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.45, rely=0.64, height=35, width=65)
        self.Button2.configure(activebackground="#f4bcb2")
        self.Button2.configure(background="wheat")
        self.Button2.configure(command=main_support.quit)
        self.Button2.configure(disabledforeground="#b8a786")
        self.Button2.configure(font=font10)
        self.Button2.configure(highlightbackground="wheat")
        self.Button2.configure(text='''Quit''')






if __name__ == '__main__':
    vp_start_gui()



