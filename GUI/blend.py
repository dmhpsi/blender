#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 10, 2018 03:36:11 PM +07  platform: Windows NT

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

from . import blend_support


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    top = Blender(root)
    blend_support.init(root, top)
    root.mainloop()


def vp_init_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    top = Blender(root)
    blend_support.init(root, top)
    return root, top


w = None


def create_Blender(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Blender(w)
    blend_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Blender():
    global w
    w.destroy()
    w = None


class Blender:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'

        top.geometry("915x748")
        top.title("Blender")
        top.configure(background="#d9d9d9")

        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.011, rely=0.0, relheight=0.989
                               , relwidth=0.809)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Result''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(width=740)

        self.can_main = Canvas(self.Labelframe1)
        self.can_main.place(relx=0.014, rely=0.027, relheight=0.959
                            , relwidth=0.973, bordermode='ignore')
        self.can_main.configure(background="#d9d9d9")
        self.can_main.configure(borderwidth="2")
        self.can_main.configure(insertbackground="black")
        self.can_main.configure(relief=RIDGE)
        self.can_main.configure(selectbackground="#c4c4c4")
        self.can_main.configure(selectforeground="black")
        self.can_main.configure(width=720)

        self.menubar = Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.831, rely=0.0, relheight=0.214
                               , relwidth=0.164)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Image 1''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(width=150)

        self.can_im1 = Canvas(self.Labelframe2)
        self.can_im1.place(relx=0.067, rely=0.125, relheight=0.831
                           , relwidth=0.887, bordermode='ignore')
        self.can_im1.configure(background="#d9d9d9")
        self.can_im1.configure(borderwidth="2")
        self.can_im1.configure(cursor="hand2")
        self.can_im1.configure(insertbackground="black")
        self.can_im1.configure(relief=RIDGE)
        self.can_im1.configure(selectbackground="#c4c4c4")
        self.can_im1.configure(selectforeground="black")
        self.can_im1.configure(width=133)

        self.Labelframe3 = LabelFrame(top)
        self.Labelframe3.place(relx=0.831, rely=0.214, relheight=0.214
                               , relwidth=0.164)
        self.Labelframe3.configure(relief=GROOVE)
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Image 2''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(width=150)

        self.can_im2 = Canvas(self.Labelframe3)
        self.can_im2.place(relx=0.067, rely=0.125, relheight=0.831
                           , relwidth=0.887, bordermode='ignore')
        self.can_im2.configure(background="#d9d9d9")
        self.can_im2.configure(borderwidth="2")
        self.can_im2.configure(cursor="hand2")
        self.can_im2.configure(insertbackground="black")
        self.can_im2.configure(relief=RIDGE)
        self.can_im2.configure(selectbackground="#c4c4c4")
        self.can_im2.configure(selectforeground="black")
        self.can_im2.configure(width=133)

        self.Labelframe4 = LabelFrame(top)
        self.Labelframe4.place(relx=0.831, rely=0.428, relheight=0.087
                               , relwidth=0.164)
        self.Labelframe4.configure(relief=GROOVE)
        self.Labelframe4.configure(foreground="black")
        self.Labelframe4.configure(text='''Position''')
        self.Labelframe4.configure(background="#d9d9d9")
        self.Labelframe4.configure(width=150)

        self.entry_pos_x = Entry(self.Labelframe4)
        self.entry_pos_x.place(relx=0.067, rely=0.462, height=24, relwidth=0.427
                               , bordermode='ignore')
        self.entry_pos_x.configure(background="white")
        self.entry_pos_x.configure(disabledforeground="#a3a3a3")
        self.entry_pos_x.configure(font="TkFixedFont")
        self.entry_pos_x.configure(foreground="#000000")
        self.entry_pos_x.configure(highlightbackground="#d9d9d9")
        self.entry_pos_x.configure(highlightcolor="black")
        self.entry_pos_x.configure(insertbackground="black")
        self.entry_pos_x.configure(selectbackground="#c4c4c4")
        self.entry_pos_x.configure(selectforeground="black")
        self.entry_pos_x.configure(width=64)

        self.entry_pos_y = Entry(self.Labelframe4)
        self.entry_pos_y.place(relx=0.533, rely=0.462, height=24, relwidth=0.427
                               , bordermode='ignore')
        self.entry_pos_y.configure(background="white")
        self.entry_pos_y.configure(disabledforeground="#a3a3a3")
        self.entry_pos_y.configure(font="TkFixedFont")
        self.entry_pos_y.configure(foreground="#000000")
        self.entry_pos_y.configure(insertbackground="black")
        self.entry_pos_y.configure(width=64)

        self.Labelframe4_25 = LabelFrame(top)
        self.Labelframe4_25.place(relx=0.831, rely=0.521, relheight=0.087
                                  , relwidth=0.164)
        self.Labelframe4_25.configure(relief=GROOVE)
        self.Labelframe4_25.configure(foreground="black")
        self.Labelframe4_25.configure(text='''Zoom''')
        self.Labelframe4_25.configure(background="#d9d9d9")
        self.Labelframe4_25.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_25.configure(highlightcolor="black")
        self.Labelframe4_25.configure(width=150)

        self.entry_zoom_x = Entry(self.Labelframe4_25)
        self.entry_zoom_x.place(relx=0.067, rely=0.462, height=24, relwidth=0.427
                                , bordermode='ignore')
        self.entry_zoom_x.configure(background="white")
        self.entry_zoom_x.configure(disabledforeground="#a3a3a3")
        self.entry_zoom_x.configure(font="TkFixedFont")
        self.entry_zoom_x.configure(foreground="#000000")
        self.entry_zoom_x.configure(highlightbackground="#d9d9d9")
        self.entry_zoom_x.configure(highlightcolor="black")
        self.entry_zoom_x.configure(insertbackground="black")
        self.entry_zoom_x.configure(selectbackground="#c4c4c4")
        self.entry_zoom_x.configure(selectforeground="black")

        self.entry_zoom_y = Entry(self.Labelframe4_25)
        self.entry_zoom_y.place(relx=0.533, rely=0.462, height=24, relwidth=0.427
                                , bordermode='ignore')
        self.entry_zoom_y.configure(background="white")
        self.entry_zoom_y.configure(disabledforeground="#a3a3a3")
        self.entry_zoom_y.configure(font="TkFixedFont")
        self.entry_zoom_y.configure(foreground="#000000")
        self.entry_zoom_y.configure(highlightbackground="#d9d9d9")
        self.entry_zoom_y.configure(highlightcolor="black")
        self.entry_zoom_y.configure(insertbackground="black")
        self.entry_zoom_y.configure(selectbackground="#c4c4c4")
        self.entry_zoom_y.configure(selectforeground="black")

        self.Labelframe4_28 = LabelFrame(top)
        self.Labelframe4_28.place(relx=0.831, rely=0.615, relheight=0.087
                                  , relwidth=0.164)
        self.Labelframe4_28.configure(relief=GROOVE)
        self.Labelframe4_28.configure(foreground="black")
        self.Labelframe4_28.configure(text='''Rotate''')
        self.Labelframe4_28.configure(background="#d9d9d9")
        self.Labelframe4_28.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_28.configure(highlightcolor="black")
        self.Labelframe4_28.configure(width=150)

        self.entry_rotate = Entry(self.Labelframe4_28)
        self.entry_rotate.place(relx=0.067, rely=0.462, height=24, relwidth=0.427
                                , bordermode='ignore')
        self.entry_rotate.configure(background="white")
        self.entry_rotate.configure(disabledforeground="#a3a3a3")
        self.entry_rotate.configure(font="TkFixedFont")
        self.entry_rotate.configure(foreground="#000000")
        self.entry_rotate.configure(highlightbackground="#d9d9d9")
        self.entry_rotate.configure(highlightcolor="black")
        self.entry_rotate.configure(insertbackground="black")
        self.entry_rotate.configure(selectbackground="#c4c4c4")
        self.entry_rotate.configure(selectforeground="black")

        self.Labelframe4_26 = LabelFrame(top)
        self.Labelframe4_26.place(relx=0.831, rely=0.709, relheight=0.087
                                  , relwidth=0.164)
        self.Labelframe4_26.configure(relief=GROOVE)
        self.Labelframe4_26.configure(foreground="black")
        self.Labelframe4_26.configure(text='''Skew''')
        self.Labelframe4_26.configure(background="#d9d9d9")
        self.Labelframe4_26.configure(highlightbackground="#d9d9d9")
        self.Labelframe4_26.configure(highlightcolor="black")
        self.Labelframe4_26.configure(width=150)

        self.entry_skew_x = Entry(self.Labelframe4_26)
        self.entry_skew_x.place(relx=0.067, rely=0.462, height=24, relwidth=0.427
                                , bordermode='ignore')
        self.entry_skew_x.configure(background="white")
        self.entry_skew_x.configure(disabledforeground="#a3a3a3")
        self.entry_skew_x.configure(font="TkFixedFont")
        self.entry_skew_x.configure(foreground="#000000")
        self.entry_skew_x.configure(highlightbackground="#d9d9d9")
        self.entry_skew_x.configure(highlightcolor="black")
        self.entry_skew_x.configure(insertbackground="black")
        self.entry_skew_x.configure(selectbackground="#c4c4c4")
        self.entry_skew_x.configure(selectforeground="black")

        self.entry_skew_y = Entry(self.Labelframe4_26)
        self.entry_skew_y.place(relx=0.533, rely=0.462, height=24, relwidth=0.427
                                , bordermode='ignore')
        self.entry_skew_y.configure(background="white")
        self.entry_skew_y.configure(disabledforeground="#a3a3a3")
        self.entry_skew_y.configure(font="TkFixedFont")
        self.entry_skew_y.configure(foreground="#000000")
        self.entry_skew_y.configure(highlightbackground="#d9d9d9")
        self.entry_skew_y.configure(highlightcolor="black")
        self.entry_skew_y.configure(insertbackground="black")
        self.entry_skew_y.configure(selectbackground="#c4c4c4")
        self.entry_skew_y.configure(selectforeground="black")

        self.btn_blend = Button(top)
        self.btn_blend.place(relx=0.831, rely=0.936, height=33, width=147)
        self.btn_blend.configure(activebackground="#d9d9d9")
        self.btn_blend.configure(activeforeground="#000000")
        self.btn_blend.configure(background="#d9d9d9")
        self.btn_blend.configure(disabledforeground="#a3a3a3")
        self.btn_blend.configure(foreground="#000000")
        self.btn_blend.configure(highlightbackground="#d9d9d9")
        self.btn_blend.configure(highlightcolor="black")
        self.btn_blend.configure(pady="0")
        self.btn_blend.configure(text='''Blend it!!!''')
        self.btn_blend.configure(width=147)


if __name__ == '__main__':
    vp_start_gui()
