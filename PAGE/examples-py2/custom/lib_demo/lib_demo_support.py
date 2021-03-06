#! /usr/bin/env python
#
# Support module generated by PAGE version 4.8a
# In conjunction with Tcl version 8.6
#    Sep 02, 2016 11:04:13 PM


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

def zoom(p1):
    print('lib_demo_support.zoom')
    global width, height
    if p1 == "in":
        width += 100
        height += 100
        refresh()
    elif p1 == "default":
        width = WIDTH
        height = HEIGHT
        refresh()
    elif p1 == "out":
        w = width - 200
        width = max(width-100, WIDTH)
        height = max(height-100, WIDTH)
        if w != 0:
            refresh()
    else:
        width = p1
        height = p1
        refresh()
        sys.stdout.flush()

def quit():
    print('lib_demo_support.quit')
    sys.stdout.flush()
    sys.exit()

def refresh():
    print('lib_demo_support.refresh')
    sys.stdout.flush()
    clean_window()
    display_buttons()

def zoom_in(p1):
    print('lib_demo_support.zoom_in')
    sys.stdout.flush()

def zoom_out(p1):
    print('lib_demo_support.zoom_out')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    display_buttons()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

WIDTH = 200
width = WIDTH
HEIGHT = 200
height = HEIGHT
pict = {}
id = {}
label = {}
num = 30

from PIL import Image, ImageTk
import tkMessageBox

# Fill the window.
def display_buttons():
   global pict, label
   pict = {}
   label = {}
   root.update_idletasks()
   frame_width = w.Custom1.window_width()
   no_thumbnails_per_row = frame_width // width
   print 'display_buttons: no_thumbnails_per_row  =', no_thumbnails_per_row    # rozen pyp

   remainder = frame_width % width
   if remainder < 10 * no_thumbnails_per_row:
       no_thumbnails_per_row -= 1
   no_thumbnails_per_row = max(no_thumbnails_per_row, 1)
   row = 0
   bg_color = top_level.cget("background")
   # For this example I only use one image and one thumbnail image
   image =  "pt-arena_hills.jpg"
   masterImg = Image.open(image)
   masterImg.thumbnail((width,height))
   thumbnail = masterImg.copy()
   original = ImageTk.PhotoImage(thumbnail)
   date = "9-24-2008"
   n = 2
   for i in range(num):
      row, col = divmod(i,no_thumbnails_per_row)
      # The expression n*rows is 2*rows, one for image and one date.
      pict[i] = Button(w.Custom1, image=original, background=bg_color)
      pict[i].image = original
      pict[i].grid(row=n*row, column=col, sticky=W+E+S+N)
      id[pict[i].winfo_id()] = i
      label[i] = Label(w.Custom1, text=date, background=bg_color)
      label[i].grid(row=n*row+1, column=col, sticky=W+E+S+N)
      pict[i].bind('<Button-1>', message)
      pict[i].bind('<Button-3>', w.popup1)
   return

def message(event):
    print 'message>event  =', event    # rozen pyp
    selected = id[event.widget.winfo_id()]
    print 'message: selected  =', selected    # rozen pyp
    tkMessageBox.showinfo("Selection", "You selected image: " + str(selected))

def clean_window():
    # Remove images from the list.
    for i in reversed(range(30)):
        try:
            pict[i].destroy()
            label[i].destroy()
        except:
            pass

# Placeholder to be replace by user definition of Custom.
Custom = Frame

# I found this code at http://tkinter.unpythonic.net/wiki/ScrolledFrame and
# just borrowed it for my photo album project. I make no claims for it.

import Tkinter
GM_KEYS = set(
        vars(Tkinter.Place).keys() +
        vars(Tkinter.Pack).keys() +
        vars(Tkinter.Grid).keys()
        )

class ScrolledFrame(object):
    _managed = False
    # XXX These could be options
    x_incr = 10
    y_incr = 10

    def __init__(self, master=None, **kw):
        print "ScrolledFrame __init__ starting."
        self.width = kw.pop('width', 200)
        self.height = kw.pop('height', 200)

        self._canvas = Tkinter.Canvas(master, **kw)
        self.master = self._canvas.master

        self._hsb = Tkinter.Scrollbar(orient='horizontal',
                command=self._canvas.xview)
        self._vsb = Tkinter.Scrollbar(orient='vertical',
                command=self._canvas.yview)
        self._canvas.configure(
                xscrollcommand=self._hsb.set,
                yscrollcommand=self._vsb.set)

        self._placeholder = Tkinter.Frame(self._canvas)
        self._canvas.create_window(0, 0, anchor='nw', window=self._placeholder)

        self._placeholder.bind('<Map>', self._prepare_scroll)
        self._placeholder.bind('<Configure>', self._prepare_scroll)
        for widget in (self._placeholder, self._canvas):
            widget.bind('<Button-4>', self.scroll_up)
            widget.bind('<Button-5>', self.scroll_down)

    def window_width(self):
        ''' Rozen. Returns the width of the scrolled window.'''
        return self._canvas.winfo_width()

    def window_height(self):
        ''' Rozen, Returns the height of scrolled window.'''
        return self._canvas.winfo_height()

    def forget_H_bar(self):
        ''' Rozen.Remove the scroll_bar.'''
        self._hsb.pack_forget()

    def remember_H_bar(self):
        self._canvas.pack_forget()
        self._hsb.pack(side='bottom', fill='x')
        self._canvas.create_window(0, 0, anchor='nw', window=self._placeholder)
        self._canvas.pack()

    def remove_V_bar(self):
        ''' Rozen.Remove the scroll_bar.'''
        self._vsb.pack_forget()

    def __getattr__(self, attr):
        if attr in GM_KEYS:
            if not self._managed:
                # Position the scrollbars now.
                self._managed = True
                if attr == 'pack':
                    self._hsb.pack(side='bottom', fill='x')
                    self._vsb.pack(side='right', fill='y')
                elif attr == 'grid':
                    self._hsb.grid(row=1, column=0, sticky='ew')
                    self._vsb.grid(row=0, column=1, sticky='ns')
                elif attr == 'place':  # Added by Rozen
                    self._hsb.pack(side='bottom', fill='x')
                    self._vsb.pack(side='right', fill='y')

            return getattr(self._canvas, attr)

        else:
            return getattr(self._placeholder, attr)


    def yscroll(self, *args):
        self._canvas.yview_scroll(*args)


    def scroll_up(self, event=None):
        self.yscroll(-self.y_incr, 'units')


    def scroll_down(self, event=None):
        self.yscroll(self.y_incr, 'units')

    def see(self, event):
        widget = event.widget
        w_height = widget.winfo_reqheight()
        c_height = self._canvas.winfo_height()
        y_pos = widget.winfo_rooty()

        if (y_pos - w_height) < 0:
            # Widget focused is above the current view
            while (y_pos - w_height) < self.y_incr:
                self.scroll_up()
                self._canvas.update_idletasks()
                y_pos = widget.winfo_rooty()
        elif (y_pos - w_height) > c_height:
            # Widget focused is below the current view
            while (y_pos - w_height - self.y_incr) > c_height:
                self.scroll_down()
                self._canvas.update_idletasks()
                y_pos = widget.winfo_rooty()


    def _prepare_scroll(self, event):
        frame = self._placeholder
        frame.unbind('<Map>')
        frame.bind
        #print "_prepare_scroll"

        if not frame.children:
            # Nothing to scroll.
            return

        for child in frame.children.itervalues():
            child.bind('<FocusIn>', self.see)
            child.bind('<Button-4>', self.scroll_up)  # Rozen
            child.bind('<Button-5>', self.scroll_down)


        new_width, new_height = frame.winfo_reqwidth(), frame.winfo_reqheight()
        self._canvas.configure(scrollregion=(0, 0, new_width, new_height),
                yscrollincrement=self.y_incr, xscrollincrement=self.x_incr)

        self._canvas.configure(width=self.width, height=self.height)

Custom = ScrolledFrame


if __name__ == '__main__':
    import lib_demo
    lib_demo.vp_start_gui()


