from tkinter import *
from tkinter import ttk
import os
import numpy
import math
import random
import sys
from pixelate import *
'''from colour_quantization import *                 
from loop import *'''
from pixelate import *

def deepFry(*args):
    image_name = image.get()
    pixel_width = pixels.get()
    grid_colour = grid.get()
    if check(readimage(image_name), int(pixel_width)) < 1:
        pass
    if check(readimage(image_name), int(pixel_width)) > 1:
        display(add_grid(enlarge(pixelate(readimage(image_name), int(pixel_width), selector_average)), grid_colour))

root = Tk()
root.title("Breading")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

image = StringVar()
image_entry = ttk.Entry(mainframe, width=17, textvariable=image)
image_entry.grid(column=2, row=1, sticky=(W, E))

colours = StringVar()
colours_entry = ttk.Entry(mainframe, width=7, textvariable=colours)
colours_entry.grid(column=2, row=2, sticky=(W, E))

pixels = StringVar()
pixels_entry = ttk.Entry(mainframe, width=7, textvariable=pixels)
pixels_entry.grid(column=2, row=3, sticky=(W, E))

grid = StringVar()
grid_entry = ttk.Entry(mainframe, width=7, textvariable=grid)
grid_entry.grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="deep fry", command=deepFry).grid(column=1, row=5, sticky=W)

ttk.Label(mainframe, text="image file").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="# of colours").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="# of units wide").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="grid colour").grid(column=1, row=4, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

image_entry.focus()
colours_entry.focus()
pixels_entry.focus()
grid_entry.focus()
root.bind("<Return>", deepFry)

root.mainloop()