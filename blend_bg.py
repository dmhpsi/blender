import cv2
from PIL import ImageTk
import PIL.Image
from GUI import *
import easygui
from tkinter import *

im1_path = None
im1 = None
root = None
top = None


def open_im1(e):
    global im1_path, im1, root, top
    im1_path = easygui.fileopenbox(filetypes=[["*.jpg", "*.png", "*.bmp", "Image Files"]])
    im1 = cv2.imread(im1_path)
    im = PIL.Image.open(im1_path).resize((top.can_im1.winfo_width(), top.can_im1.winfo_height()), PIL.Image.ANTIALIAS)
    top.im1 = ImageTk.PhotoImage(im)
    top.can_im1.delete("IMG")
    top.can_im1.create_image(0,
                             0,
                             anchor=NW,
                             image=top.im1,
                             tags="IMG")
    root.update()


def open_im2(e):
    print(e)


if __name__ == '__main__':
    root, top = blend.vp_init_gui()
    top.can_im1.bind("<Button-1>", open_im1)
    top.can_im2.bind("<Button-1>", open_im2)
    root.mainloop()
