import cv2
from PIL import ImageTk
import PIL.Image
from GUI import *
import easygui
from tkinter import *
import numpy as np

im1_path = None
root = None
top = None
blended_rgb = None


def open_im1(e):
    global im1_path, root, top
    im1_path = easygui.fileopenbox(filetypes=[["*.jpg", "*.png", "*.bmp", "Image Files"]])
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


def save_result(e):
    global blended_rgb
    res_path = easygui.filesavebox()
    cv2.imwrite(res_path, blended_rgb)


def parse_float(inp):
    try:
        return float(inp)
    except:
        return float(0)


def blend_images(e):
    global top, blended_rgb
    im1 = cv2.imread("D:/pi/rgb.jpg")  # color image
    im1_width, im1_height, _ = im1.shape
    im1_hsv = cv2.cvtColor(im1, cv2.COLOR_RGB2HSV)
    im1_h, im1_s, im1_v = cv2.split(im1_hsv)
    im1_r, im1_g, im1_b = cv2.split(im1)
    im2 = cv2.imread("D:/pi/thermal.jpg")  # thermal image
    resized_im2 = cv2.resize(src=im2, dsize=(im1_height, im1_width), interpolation=cv2.INTER_LANCZOS4)
    resized_im2_gray = cv2.cvtColor(resized_im2, cv2.COLOR_RGB2GRAY)
    # blended_hsv = cv2.merge([im1_h, im1_s, im1_v])
    # blended_rgb = cv2.cvtColor(blended_hsv, cv2.COLOR_HSV2BGR)
    new_r = (np.array(im1_r) + np.array(resized_im2_gray)) / 2.0
    im1_r = new_r.astype(np.uint8)
    blended_rgb = cv2.merge([resized_im2_gray, im1_g, im1_b])

    im = PIL.Image.fromarray(blended_rgb).resize((top.can_main.winfo_width(), top.can_main.winfo_height()), PIL.Image.ANTIALIAS)
    top.im_main = ImageTk.PhotoImage(im)
    top.can_main.delete("IMG")
    top.can_main.create_image(0,
                              0,
                              anchor=NW,
                              image=top.im_main,
                              tags="IMG")


if __name__ == '__main__':
    root, top = blend.vp_init_gui()
    top.can_im1.bind("<Button-1>", open_im1)
    top.can_im2.bind("<Button-1>", open_im2)
    top.can_main.bind("<Button-1>", save_result)
    top.btn_blend.bind("<Button-1>", blend_images)
    root.mainloop()
