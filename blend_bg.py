import cv2
from PIL import ImageTk
import PIL.Image
from GUI import *
import easygui
from tkinter import *
import numpy as np
from easydict import EasyDict as edict

im1_path = ""
im2_path = ""
im1 = edict()
im2 = edict()
root = None
top = None
blended_rgb = None


def init_im(im):
    im.nw_x = 0
    im.nw_y = 0
    im.sw_x = 0
    im.sw_y = 299
    im.ne_x = 399
    im.ne_y = 0
    im.se_x = 399
    im.se_y = 299


def open_im(e):
    global im1_path, im2_path, im1, im2, top
    im_path = easygui.fileopenbox(default="D:/pi/",
                                  filetypes=[["*.jpg", "*.png", "*.bmp", "Image Files"], ["*.*", "All files"]])
    im_in = cv2.imread(im_path)
    im = cv2.cvtColor(im_in, cv2.COLOR_BGR2RGB)
    pers = cv2.resize(im, (400, 300), interpolation=cv2.INTER_LANCZOS4)
    if e.widget == top.btn_open_im1:
        im1_path = im_path
        init_im(im1)
        im1.im = im
        im1.pers = pers
        top.im1 = ImageTk.PhotoImage(PIL.Image.fromarray(pers))
        top.can_im1.delete("IMG")
        top.can_im1.create_image(0, 0, anchor=NW, image=top.im1, tags="IMG")
    else:
        im2_path = im_path
        init_im(im2)
        im2.im = im
        im2.pers = pers
        top.im2 = ImageTk.PhotoImage(PIL.Image.fromarray(pers))
        top.can_im2.delete("IMG")
        top.can_im2.create_image(0, 0, anchor=NW, image=top.im2, tags="IMG")
    root.update()


def save_result(e):
    global blended_rgb
    res_path = easygui.filesavebox(filetypes=[["*.jpg", "*.png", "*.bmp", "Image Files"]])
    cv2.imwrite(res_path, blended_rgb)


def parse_float(inp):
    try:
        return float(inp)
    except:
        return float(0)


def blend_images(e):
    global top, blended_rgb, im1, im2
    im1_r, im1_g, im1_b = cv2.split(im1.pers)
    resized_im2_gray = cv2.cvtColor(im2.pers, cv2.COLOR_RGB2GRAY)
    blended_rgb = cv2.merge([resized_im2_gray, im1_g, im1_b])

    im = PIL.Image.fromarray(blended_rgb)
    top.im_main = ImageTk.PhotoImage(im)
    top.can_main.delete("IMG")
    top.can_main.create_image(0,
                              0,
                              anchor=NW,
                              image=top.im_main,
                              tags="IMG")


def im_selector(e):
    if e.widget == top.can_im1:
        im = im1
    else:
        im = im2
    maxw = 400
    maxh = 300
    if e.x <= maxw / 2:
        if e.y <= maxh / 2:
            im.nw_x = e.x
            im.nw_y = e.y
        else:
            im.sw_x = e.x
            im.sw_y = e.y
    else:
        if e.y <= maxh / 2:
            im.ne_x = e.x
            im.ne_y = e.y
        else:
            im.se_x = e.x
            im.se_y = e.y
    canvas_update(im, e.widget)


def canvas_update(im, can):
    maxw = 400
    maxh = 300
    ih, iw, _ = im.im.shape
    ratiox = float(iw) / maxw
    ratioy = float(ih) / maxh
    can.delete("poly")
    can.poly = can.create_polygon([im.nw_x, im.nw_y,
                                   im.ne_x, im.ne_y,
                                   im.se_x, im.se_y,
                                   im.sw_x, im.sw_y],
                                  outline="#ff0000",
                                  fill="",
                                  tags="poly")
    pts1 = np.float32([[im.nw_x * ratiox, im.nw_y * ratioy],
                       [im.ne_x * ratiox, im.ne_y * ratioy],
                       [im.sw_x * ratiox, im.sw_y * ratioy],
                       [im.se_x * ratiox, im.se_y * ratioy]])
    pts2 = np.float32([[0, 0], [400, 0], [0, 300], [400, 300]])
    mat = cv2.getPerspectiveTransform(pts1, pts2)
    im.pers = cv2.warpPerspective(im.im, mat, (400, 300))


if __name__ == '__main__':
    root, top = blend.vp_init_gui()
    init_im(im1)
    init_im(im2)
    top.btn_open_im1.bind("<Button-1>", open_im)
    top.btn_open_im2.bind("<Button-1>", open_im)
    top.btn_export.bind("<Button-1>", save_result)
    top.btn_blend.bind("<Button-1>", blend_images)
    top.can_im1.bind("<Button-1>", im_selector)
    top.can_im2.bind("<Button-1>", im_selector)
    root.mainloop()
