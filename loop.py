from PIL import Image
import os
import sys
import numpy
import math
import random
from pixelate import readimage
from pixelate import display
from colour_quantization import *

def cutList(image):
    long_pixels = makePixelList(image)
    sorted_pixels = sortBig(long_pixels)
    sorted_first = cutFirstList(sorted_pixels)
    sorted_second = cutSecondList(sorted_pixels)
    return (sorted_first, sorted_second)

def loopColourQuantization(picture, loopamount):
    # final list of pieces
    final_pieces = []
    # temporary pieces
    pieces = []
    for num in range(loopamount):
        # cutting long_pixels into two
        first = cutList(picture)[0]
        second = cutList(picture)[1]
        # putting the pieces into one list
        pieces.append(first)
        pieces.append(second)
        pieces.append(final_pieces)

        # finding difference key for each piece
        differences = {}
        for item in pieces:
            # print(item)
            diff_key = findDifference(item)[0]
            diff_value = findDifference(item)[1]
            differences[diff_key] = diff_value

        # finding the biggest difference key
        for key, value in differences.items():
            big = 0
            if value > big:
                big = value

        # finding the key and value for the difference key
        for key, value in differences.items():
            if value == big:
                largest_difference_key = key
                largest_difference_value = value

        # finding the index of the difference key (should match with pieces)
        i = 0
        final_i = 0
        for key, value in differences.items():
            if largest_difference_key == key:
                if largest_difference_value == value:
                    final_i = i
                    break
            i = i + 1

        # sorting pieces into final_pieces and long_pixels
        for num in range(len(pieces)):
            if num == final_i:
                long_pixels = pieces[final_i]
            else:
                final_pieces.append(pieces[num])
    return final_pieces

def findAverageColour1(pixels):
    first_r = 0
    first_g = 0
    first_b = 0
    for item in first:
        first_r = first_r + item["r"]
        first_g = first_g + item["g"]
        first_b = first_b + item["b"]
    first_final_r = first_r / len(first)
    first_final_g = first_g / len(first)
    first_final_b = first_b / len(first)
    return (first_final_r, first_final_g, first_final_b)

def implementAverageColour1(originalpixel, average_colours, newpixels):
    # contains the average rgb values for first and second lists
    for item in newpixels:
        for colour in item:
            item["r"] = average_colours[0]
            item["g"] = average_colours[1]
            item["b"] = average_colours[2]
            originalpixel[item["x"]][item["y"]] = (item["r"], item["g"], item["b"])
    return originalpixel

# colours = newpixels, average_colours = avg_colours, originalpixel = originalpixel

'''def loopDisplay(final_pieces, originalpixel):
    for colours in final_pieces:
        avg_colours = findAverageColour1(colours)
        implementAverageColour1(originalpixel, avg_colours, colours)
    return originalpixel'''




# returns tuple of averages for first and second rgb values
'''average_colour = findAverageColour(sorted_first, sorted_second)
fr = final_average_colours[0]
fg = final_average_colours[1]
fb = final_average_colours[2]
sr = final_average_colours[3]
sg = final_average_colours[4]
sb = final_average_colours[5]

for num in range(loopamount):
    loopColourQuanitzation'''
