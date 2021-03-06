#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.27d
#  in conjunction with Tcl version 8.6
#    Nov 20, 2019 09:39:45 PM PST  platform: Linux

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

def on_btnExit():
    sys.exit()

def quit():
    sys.exit()

def refresh():
    clean_window()
    display_buttons()

def zoom(p1):
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

w = 3
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    display_buttons()

WIDTH = 200
width = WIDTH
HEIGHT = 200
height = HEIGHT
pict = {}
id = {}
label = {}
num = 30

from PIL import Image, ImageTk
import tkinter.messagebox

def display_buttons():
   # Fill the window.
   # For this example I only use one image and one thumbnail image.
   global pict, label
   inner_frame = w.Scrolledwindow1_f
   pict = {}
   label = {}

   no_thumbnails_per_row = 2
   bg_color = top_level.cget("background")
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
      pict[i] = tk.Button(inner_frame, image=original, background=bg_color)
      pict[i].image = original
      pict[i].grid(row=n*row, column=col, sticky='wesn')
      id[pict[i].winfo_id()] = i
      label[i] = tk.Label(inner_frame, text=date, background=bg_color)
      label[i].grid(row=n*row+1, column=col, sticky='wesn')
      pict[i].bind('<Button-1>', message)
      pict[i].bind('<Button-3>', w.popup1)
   # Magic which ties widget scrollbars to dimensions of the inner_frame.
   pict[0].wait_visibility()
   bbox = inner_frame.bbox()
   w.Scrolledwindow1.configure(scrollregion=bbox)

def message(event):
    selected = id[event.widget.winfo_id()]
    print('message: selected  =', selected)    # rozen pyp
    tkinter.messagebox.showinfo("Selection",
                                "You selected image: " + str(selected))

def clean_window():
    # Remove images from the widget.
    for i in reversed(list(range(num))):
        try:
            pict[i].destroy()
            label[i].destroy()
        except:
            pass

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import new
    new.vp_start_gui()





