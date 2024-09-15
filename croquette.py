import os
import numpy
import math
import random
import sys
from pixelate import *
from colour_quantization import *
from loop import *
from pixelate import *

picture = "tree.jpg"
loop_amount = 4
pixelwidth = 50
gridcolour = "black"

# BEEP BEEP BOOP BOOP

def run():
    if len(sys.argv) == 1:
        print('\n'
              'Welcome to Croquette, a program that utilises user provided images to generate crochet tapestry patterns. \n'
              'To utilise this program, please provide: \n'
              'Name of the image file (if your file name has spaces, please put it in "") \n'
              'Desired number of squares wide \n'
              'Desired colour of the grid lines (black/white) \n'
              'These three items should follow the the name of this program, each separated with a space. \n'
              'For example: python main.py "cat picture.png" 50 black. \n'
              'Please note: If the original width of the photo provided divided by the desired amount of squares wide is smaller than 1, this program will not work. ')

    elif len(sys.argv) < 4:
        print('You have provided too few arguments. Please check your input and try again.')
    elif len(sys.argv) > 4:
        print('You have provided too many arguments. Please check your input and try again.')

    else:
        filename = sys.argv[1]
        pixelwidth = sys.argv[2]
        gridcolour = sys.argv[3]
        # loopamount = sys.argv[4]
        if check(readimage(filename), int(pixelwidth)) < 1:
            print("The desired final width is too large and results in an error. \n"
                  "Please reduce the final width desired so that the original width divided by the final width is greater than 1.")
        if check(readimage(filename), int(pixelwidth)) > 1:
            display(add_grid(enlarge(pixelate(readimage(filename), int(pixelwidth), selector_average)), gridcolour))

'''def displayColours(): # idk what this is
    original_list = readimage(picture)
    massive_list = makePixelDict(picture)
    sorted_list = sortBig(massive_list)
    first_list = cutFirstList(sorted_list)
    second_list = cutSecondList(sorted_list)
    average_colours = findAverageColour(first_list, second_list)
    implemented_colours = implementAverageColour(original_list, average_colours, first_list, second_list)
    return display(implemented_colours)'''

def quantizeColours():
    originalpixel = readimage(picture)
    originaldict = makePixelDict(originalpixel)
    chopped_pieces = loopColourQuantization(originaldict, loop_amount)
    doColours(chopped_pieces, originalpixel)
    return originalpixel

# run()
# displayLoop()
display(add_grid(enlarge(pixelate(quantizeColours(), int(pixelwidth), selector_middle)), gridcolour))