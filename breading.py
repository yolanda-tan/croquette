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
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def deepFry(*args):
    image_name = image_result.get()
    bar.step(20)
    pixel_width = pixels.get()
    bar.step(40)
    grid_colour = grid.get()
    bar.step(60)
    if check(readimage(image_name), int(pixel_width)) < 1:
        pass
    bar.step(80)
    if check(readimage(image_name), int(pixel_width)) > 1:
        display(add_grid(enlarge(pixelate(readimage(image_name), int(pixel_width), selector_average)), grid_colour))
    bar.step(99.9)

root = Tk()
root.title("Breading")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def submitIngredients():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    image_result.set(filename)

image_result = StringVar()
ttk.Label(mainframe, textvariable=image_result).grid(column=1, row=2, columnspan = 2, sticky=(W, E))

image_entry = ttk.Button(mainframe, width=17, text='select', command=submitIngredients)
image_entry.grid(column=2, row=1, sticky=(W, E))


colours = StringVar()
colours_entry = ttk.Entry(mainframe, width=17, textvariable=colours)
colours_entry.grid(column=2, row=3, sticky=(W, E))

pixels = StringVar()
pixels_entry = ttk.Entry(mainframe, width=17, textvariable=pixels)
pixels_entry.grid(column=2, row=4, sticky=(W, E))

grid = StringVar()
grid_entry = ttk.Combobox(mainframe, width=17, textvariable=grid)
grid_entry['values'] = ('black', 'white')
grid_entry.state(["readonly"])
grid_entry.grid(column=2, row=5, sticky=(W, E))

bar = ttk.Progressbar(mainframe, orient=HORIZONTAL, style='success.Striped.Horizontal.TProgressbar', length=300, mode='determinate')
bar.grid(column=1, row=7, columnspan = 2, sticky=(W))

ttk.Button(mainframe, text="deep fry", command=deepFry).grid(column=1, row=6, sticky=W)

ttk.Label(mainframe, text="image file").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="# of colours").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="# of units wide").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="grid colour").grid(column=1, row=5, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

image_entry.focus()
root.bind("<Return>", deepFry)

root.mainloop()