from PIL import Image
import os
import sys
import numpy
import math
import random

WIDTH = 500
HEIGHT = 500
# scale must be positive integer (no decimals or fractions)
SCALE = 25

'cat picture.png'


original = [
    [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
    [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
    [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
    [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
]

def enlarge(original):
    original_height = len(original)
    original_width = len(original[0])
    final_height = original_height*SCALE
    final_width = original_width*SCALE

    pixels = []
    for num in range(final_height):
        row = []
        for num in range(final_width):
            colour = (0, 0, 0)
            row.append(colour)
        pixels.append(row)


    for i, row in enumerate(original):
        for j, colour in enumerate(row):
            for y in range(SCALE):
                for x in range(SCALE):
                    new_i = i*SCALE + y
                    new_j = j*SCALE + x
                    pixels[new_i][new_j] = colour
    return pixels
    #print(pixels)


def display(pixels):
    pixel_array = numpy.array(pixels, dtype=numpy.uint8)
    new_image = Image.fromarray(pixel_array)
    new_image.show()

#enlarge(original)

def readimage(image):
    i = Image.open(image)

    pixels = i.load()
    width, height = i.size

    all_pixels = []
    for y in range(height):
        newlist = []
        for x in range(width):
            cpixel = pixels[x, y]
            newlist.append(cpixel)
        all_pixels.append(newlist)
    return all_pixels
#all pixels = massive image


def selector_top_left(sector):
    top_left = sector[0]
    return (top_left[0], top_left[1], top_left[2])

def selector_middle(sector):
    middle = sector[math.floor(len(sector)/2)]
    return (middle[0], middle[1], middle[2])

def selector_random(sector):
    return sector[random.randint(0, len(sector)-1)]

def selector_average(sector):
    r = 0
    g = 0
    b = 0
    for item in sector:
        r = r + item[0]
        g = g + item[1]
        b = b + item[2]
    final_r = r/len(sector)
    final_g = g/len(sector)
    final_b = b/len(sector)
    return (final_r, final_g, final_b)

def check(large, final_width):
    final_scale = len(large[0])/final_width
    return final_scale

def pixelate(large, final_width, selector):
    pixels = []
    original_width = len(large[0])
    original_height = len(large)
    final_height = math.floor((final_width*original_height)/original_width)
    for num in range(final_height):
        row = []
        for num in range(final_width):
            colour = (0, 0, 0)
            row.append(colour)
        pixels.append(row)

    final_scale = original_width/final_width

    # pixels = final
    # large is the original
    for i, row in enumerate(pixels):
        for j, colour in enumerate(row):
            new_low_i = i*final_scale
            new_low_j = j*final_scale
            new_high_i = (i*final_scale) + (final_scale - 1)
            new_high_j = (j*final_scale) + (final_scale - 1)
            #print(f"{new_low_i} {new_high_i} {new_low_j} {new_high_j}")
            sector = []
            for x in range(math.floor(new_low_i), math.ceil(new_high_i)):
                for y in range(math.floor(new_low_j), math.ceil(new_high_j)):
                    sector.append(large[x][y])
            pixels[i][j] = selector(sector)
    return pixels

# can only call this on already enlarged pictures
def add_grid(enlarged_picture, grid_colour_input):
    grid_line_colour = ()
    if grid_colour_input.lower() == 'white':
        grid_line_colour = (255, 255, 255)
    if grid_colour_input.lower() == 'black':
        grid_line_colour = (0, 0, 0)
    for i, row in enumerate(enlarged_picture):
        for j, colour in enumerate(row):
            sector = []
            if i % SCALE == SCALE - 1:
                enlarged_picture[i][j] = grid_line_colour
            if j % SCALE == SCALE - 1:
                enlarged_picture[i][j] = grid_line_colour
            if i % SCALE == 0:
                enlarged_picture[i][j] = grid_line_colour
            if j % SCALE == 0:
                enlarged_picture[i][j] = grid_line_colour
    return(enlarged_picture)
