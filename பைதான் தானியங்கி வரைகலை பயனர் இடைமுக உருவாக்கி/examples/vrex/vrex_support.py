#! /usr/bin/env python
#
# Generated by PAGE version 4.2
# In conjunction with Tcl version 8.6
#    Jan. 10, 2014 10:11:31 PM


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

import vrex_help
from tkinter import filedialog
#import tkFileDialog

def clear_textbox(o):
    o.delete(1.0, END)


def init(tk_root,gui):
    global w, root
    w = gui
    root = tk_root
    # This is executed after the GUI is drawn.
    global colors, color_noreport, color_lookahead, levels, o_e, o_s, o_m
    # Define the object names for the three text windows;
    o_e = w.Expression
    o_s = w.Sample
    o_m = w.Matches
    # the colors for the different matching groups
    colors = ['red', 'blue', 'darkgreen', 'magenta', 'sienna', 'purple',
              'firebrick', 'deeppink', 'deeppink', 'deepskyblue1']
    # background color to visualize the non-reporting group (?:...)
    color_noreport = 'cyan'
    # background color to visualize the lookhead group (?=...) and (?!...)
    color_lookahead = 'plum'
    # define levels
    levels = ['e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9']
    # configure the tags to be used.
    for i in range(len(levels)):
        o_e.tag_configure(levels[i], foreground=colors[i])
        o_s.tag_configure(levels[i], foreground=colors[i])
        o_m.tag_configure(levels[i], foreground=colors[i])
    o_e.tag_configure('lookahead', background=color_lookahead)
    o_e.tag_configure('noreport', background=color_noreport)


def insert_text(o, str):
    o.insert(END, str)


def display(level):
    go()
    clear_textbox(o_m)
    for i in range(len(mo)-1):
        if mo[i] == None:
            insert_text(o_m, "Match failed\n")
        else:
            if level <= len(mo[i].groups()):
                # Insert the text corresponding to the match group.
                start, end = mo[i].span(level)
                str = s_lines[i][start:end]
                insert_text(o_m, str+'\n')
                line = '%d.0' % (i+1,)
                last = '%d.%d' % (i+1,end)
                o_m.tag_add(levels[level], line, last) # Colorize text.

def do_match():
    import re
    global mo, rexp, sample, s_lines
    rexp = read_textbox(o_e)
    rexp = rexp.strip()
    sample = read_textbox(o_s)
    s_lines = sample.split('\n')
    rc = re.compile(rexp)
    mo = []
    for line in s_lines:
        mo.append(rc.search(line))

def go():
    regexp_colorize()
    do_match()
    sample_colorize()

def help():
    vrex_help.create_Toplevel1(root)

def load_regular_expression():
    regex_file = filedialog.askopenfilename(filetypes=[("all files", "*")])
    if regex_file:
        clear_textbox(o_e)
        rd = open(regex_file)
        exp = rd.read()
        o_e.insert(END,exp)
        rd.close()

def load_sample():
    sample_file = filedialog.askopenfilename(filetypes=[("all files", "*")])
    if sample_file:
        clear_textbox(o_s)
        sd = open(sample_file)
        sample = sd.read()
        sample = sample.rstrip()
        o_s.insert(END,sample)

def quit():
    import sys
    sys.exit()

def read_textbox(o):
    # Note how one can read all of the characters from a text box. The
    # 1.0 refers to the first character (line position 0) in vTclthe first
    # line (line 1).
    return o.get(1.0, END)
def regexp_colorize():
    global nblevels
    import types
    stack = []
    indicies = []
    # The format of indicies is a list of tuple each looking like
    # (type, min, max). Type can be report, no report, or lookahead.
    exp = read_textbox(o_e).rstrip()
    indicies.append(('report', 0, len(exp)))
    nblevels = 1
    for i in range(len(exp)):
        c = exp[i]
        if c == '\\':
            i += 1
            continue
        elif c == '(':
            c = exp[i+1]
            if c == '?':
                what = exp[1+2]
                if what == ':':
                    type = 'lookahead'
                else:
                    type = 'noreport'
            else:
                type = 'report'
            nblevels += 1
            min = i
            max = 0
            indicies.append((type, min, max))
            stack.append(len(indicies)-1)
        elif c == ')':
            idx = stack.pop()
            type, min, max = indicies[idx]
            indicies[idx] = (type, min, i)
    # Remove old colors.
    for level in range(nblevels):
        o_e.tag_remove(levels[level], 1.0, END)
    o_e.tag_remove("lookahead", 1.0, END)
    o_e.tag_remove("noreport", 1.0, END)
    # Colorize the regular expression
    i = 0
    for type,min,max in indicies:
        min_c = '1.0+%dchars' % min
        max_1 = max + 1
        max_c = '1.0+%dchars' % max_1
        o_e.tag_add(levels[i], min_c, max_c)
        i += 1
    # Colorize special items.
    for type,min,max in indicies:
        if type == 'report':
            continue
        min_c = '1.0+%dchars' % min
        max_1 = max + 1
        max_c = '1.0+%dchars' % (max + 1,)
        o_e.tag_add(type, min_c, max_c)
def sample_colorize():
    # Remove colors
    for level in range(nblevels):
        o_s.tag_remove(levels[level], 1.0, END)
    for i in range(len(mo)):
        if mo[i] == None:
            continue
        # Add the new colors
        if level <= len(mo[i].groups()):
            for level in range(nblevels):
                start, end = mo[i].span(level)
                min_c = '%d.0+%dchars' % (i+1, start)
                max_c = '%d.0+%dchars' % (i+1, end)
                o_s.tag_add(levels[level], min_c, max_c)


def save_regular_expression():
    regex_file = tkFileDialog.asksaveasfilename(filetypes=[("all files", "*")])
    if regex_file:
        rd = open(regex_file, 'w')
        rxp = read_textbox(o_e)
        rd.write(rxp)
        rd.close()

def save_sample():
    sample_file = tkFileDialog.asksaveasfilename(filetypes=[("all files", "*")])
    if sample_file:
        sd = open(sample_file, 'w')
        sample = read_textbox(o_s)
        sd.read(sample)
        sd.close()

def sync_matches(p1):
    ''' Function which makes sure that line in Matches corresponding
        to the like selected with button-1 in Sample is visible.'''
    index = w.Sample.index(CURRENT)
    w.Matches.see(index)

def sync_sample(p1):
    ''' Function which makes sure that line in Sample corresponding to
        the like selected with button-1 in Matches is visible.'''
    index = w.Matches.index(CURRENT)
    line, char = index.split('.')
    w.Sample.see(index)

