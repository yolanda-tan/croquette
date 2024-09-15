from PIL import Image
import os
import sys
import numpy
import math
import random
from pixelate import readimage
from pixelate import display
from colour_quantization import *

'''def cutPieces(image):
    long_pixels = makePixelList(image)
    # long_pixels = dictionaries of rgb and xy values
    sorted_pixels = sortBig(long_pixels)
    sorted_first = cutFirstList(sorted_pixels)
    sorted_second = cutSecondList(sorted_pixels)
    return (sorted_first, sorted_second)'''

# loopamount = # of times the pixel_list is cut (# of colours in the final picture subtracting one)
# pixel_list = list of pixel values for the entire image
def loopColourQuantization(pixel_list, loopamount):
    # NOT FINISHED
    # pieces = lists of dictionaries that contain rgbxy values. each list is a section of the original pixel list.
    pieces = [pixel_list]
    for number in range(loopamount):
        # call a function that cuts the largest hunk in pieces into 2 chunks
        cutPieces(pieces)
    return pieces

# putting average colours of each piece into the original pixel grid
# list_of_pieces = list of all cut up pieces
# originalpixel = grid of original pixels (list of rows/2d)
def doColours(list_of_pieces, originalpixel):
    # find average colour of each piece
    for hunk in list_of_pieces:
        avg_colour = findAverageColour1(hunk)
        for pixel_dict in hunk:
            x = pixel_dict["x"]
            y = pixel_dict["y"]
            originalpixel[x][y] = avg_colour
    # for each piece, do the colour back into the original pixel grid

# find the key with the largest difference in each list, then find the piece with the largest difference in terms of the key.
# cut the piece into two new pieces
# replace the old piece with the two new pieces
def cutPieces(pieces):
    big = 0 # value of the difference
    big_diff_key = "" # key of the chunk with the biggest difference in pieces
    big_index = 0 # index of the biggest chunk in pieces
    for c, chunk in enumerate(pieces):
        diff_key, diff_value = findDifference(chunk)
        if diff_value > big:
            big = diff_value
            big_diff_key = diff_key
            big_index = c
    # sort
    sorted_largest_list = sortBig(big_diff_key, pieces[big_index])
    # now we cut
    first_half = cutFirstList(sorted_largest_list)
    second_half = cutSecondList(sorted_largest_list)
    pieces[big_index] = first_half
    pieces.append(second_half)










'''def loopColourQuantization(picture, loopamount):
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
        differences = []
        for item in pieces:
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
    return final_pieces'''

def findAverageColour1(pixels):
    first_r = 0
    first_g = 0
    first_b = 0
    for item in pixels:
        first_r = first_r + item["r"]
        first_g = first_g + item["g"]
        first_b = first_b + item["b"]
    first_final_r = first_r / len(pixels)
    first_final_g = first_g / len(pixels)
    first_final_b = first_b / len(pixels)
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
