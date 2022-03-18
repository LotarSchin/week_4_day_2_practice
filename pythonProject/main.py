import random
from tkinter import *
from colorsys import hls_to_rgb

def rgb_int_to_hex(rgb):
    #translates an rgb tuple of int to a tkinter friendly color code
    return "#%02x%02x%02x" % rgb

def draw_stars(canvas):
    canvas.destroy()

    canvas = Canvas(root, width=w, height=h, bg='Black')
    canvas.pack()
    for i in range(100, 500):
        #  - The stars should have random positions on the canvas
        star_top = random.randint(1, w - star_size)
        star_left = random.randint(1, h - star_size)

        #  - The stars should have random color (some shade of grey)
        my_shade = random.randint(50, 255)
        my_rect = canvas.create_rectangle(star_top, star_left, star_top + star_size, star_left + star_size,
                                          fill=rgb_int_to_hex((my_shade, my_shade, my_shade)))

    # create a button
    my_btn = Button(root, text='Draw stars', width=20, height=1, bd='2', command=lambda: draw_stars(canvas))
    my_btn.place(x=2, y=2)


root = Tk()
# give a title
root.title("Starry nights")

# define our window size
w = 750
h = 280

# define canvas
# Draw the night sky:
#  - The background should be black
canvas = Canvas(root, width=w, height=h, bg='Black')
canvas.pack()

# define star
#  - The stars should be small squares
star_size = 2

# create a button
my_btn = Button(root, text='Draw stars', width=20, height=1, bd='2', command=lambda: draw_stars(canvas))
my_btn.place(x=2, y=2)

root.mainloop()