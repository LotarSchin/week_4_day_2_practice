import random
from tkinter import *
from colorsys import hls_to_rgb

min_stars = 1000
max_stars = 5000

def rgb_int_to_hex(rgb):
    #translates an rgb tuple of int to hex
    return "#%02x%02x%02x" % rgb

def draw_canvas(root, ws, hs):
    # define canvas
    # Draw the night sky:
    #  - The background should be black
    canvas = Canvas(root, width=ws, height=hs, bg='Black')
    canvas.pack()
    return canvas

def place_button(root, canvas, ws, hs):
    my_btn = Button(root, text='Draw stars', width=20, height=1, bd='2', command=lambda: draw_stars(root, canvas, ws, hs, min_stars, max_stars))
    my_btn.place(x=2, y=2)

def set_window_pos(root, ws, hs):
    # position to the center
    x = (ws / 2) - (ws / 4)
    y = (hs / 2) - (hs / 4)
    root.geometry('%dx%d+%d+%d' % (ws/2, hs/2, x, y))


def draw_stars(root, canvas, ws, hs, min, max):
    canvas.destroy()

    canvas = Canvas(root, width=ws, height=hs, bg='Black')
    canvas.pack()
    for i in range(min, max):
        #  - The stars should have random positions on the canvas
        star_top = random.randint(1, ws - star_size)
        star_left = random.randint(1, hs - star_size)

        #  - The stars should have random color (some shade of grey)
        my_shade = random.randint(50, 255)
        my_rect = canvas.create_rectangle(star_top, star_left, star_top + star_size, star_left + star_size,
                                          fill=rgb_int_to_hex((my_shade, my_shade, my_shade)))

    place_button(root, canvas, ws, hs)

root = Tk()
# give a title
root.title("Starry nights")

# define star
#  - The stars should be small squares
star_size = 2

# query display size
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# draw canvas
canvas = draw_canvas(root, ws/2, hs/2)

# create a button
place_button(root, canvas, ws, hs)

# set window pos
set_window_pos(root, ws, hs)

# show window
root.mainloop()