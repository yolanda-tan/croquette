# turn 2d grid of pixels into 1d list of pixels
# make each item in list a dictionary that contains: r, g, b, x, y values (x and y for 2d list)
# - REPEATABLE PART -
# sort 1d list by red values
# determine largest difference of values between r, g, b and sort by the one with the largest difference
# cut the list in half
# -
# for each half, find the average colour
# make all colours on that side the average colour back on the original 2d grid of pixels
# tada!

from PIL import Image
import os
import sys
import numpy
import math
import random
from pixelate import readimage
from pixelate import display

# also retain x and y
def makePixelDict(pixel_list):
    massive_tuple_list = []
    for x, row in enumerate(pixel_list):
        for y, colour in enumerate(row):
            newtuple = (colour[0], colour[1], colour[2], x, y)
            massive_tuple_list.append(newtuple)
    # massive_list is tuples of: (r, g, b, x, y)
    massive_dict_list = []
    for tuple in massive_tuple_list:
        new_dict = {"r": tuple[0], "g": tuple[1], "b": tuple[2], "x": tuple[3], "y": tuple[4]}
        massive_dict_list.append(new_dict)
    return massive_dict_list

# finding key to sort by
def findDifference(massivedictlist):
    values = ["r", "g", "b"]
    difference_dict = {"r":0, "g": 0, "b": 0}
    for colour in values:
        # big
        big = 0
        for item in massivedictlist:
            if item[colour] > big:
                big = item[colour]
        # small
        small = 255
        for item in massivedictlist:
            if item[colour] < small:
                small = item[colour]
        difference = big - small
        difference_dict[colour] = difference
    largest_difference = 0
    for colour_difference in difference_dict.values():
        if colour_difference > largest_difference:
            largest_difference = colour_difference
    largest_difference_key = ""
    largest_difference_value = 0
    for key, value in difference_dict.items():
        if value == largest_difference:
            largest_difference_key = key
            largest_difference_value = value
    return largest_difference_key, largest_difference_value

# sorting the list by the key with the most difference

def sorter_red(item):
  return item["r"]
def sorter_green(item):
  return item["g"]
def sorter_blue(item):
  return item["b"]
def sortByKeyRed(pixels):
    pixels.sort(key=sorter_red)
    return pixels
def sortByKeyGreen(pixels):
    pixels.sort(key=sorter_green)
    return pixels
def sortByKeyBlue(pixels):
    pixels.sort(key=sorter_blue)
    return pixels

'''def sortBig(pixels):
    if findDifference(pixels)[0] == "r":
        return sortByKeyRed(pixels)
    if findDifference(pixels)[0] == "g":
        return sortByKeyGreen(pixels)
    if findDifference(pixels)[0] == "b":
       return sortByKeyBlue(pixels)'''

def sortBig(big_diff_key, pixels):
    if big_diff_key == "r":
        return sortByKeyRed(pixels)
    if big_diff_key == "g":
        return sortByKeyGreen(pixels)
    if big_diff_key == "b":
       return sortByKeyBlue(pixels)

# cutting the sorted list into two (pixels = sorted list)
def cutFirstList(pixels):
    middle = round(len(pixels)/2)
    first_half = []
    for num in range(middle):
        first_half.append(pixels[num])
    return first_half
def cutSecondList(pixels):
    middle = round(len(pixels)/2)
    second_half = []
    for num in range(middle, len(pixels)):
        second_half.append(pixels[num])
    return second_half

# finding the average colour of both the lists
def findAverageColour(first, second):
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
    second_r = 0
    second_g = 0
    second_b = 0
    for item in second:
        second_r = second_r + item["r"]
        second_g = second_g + item["g"]
        second_b = second_b + item["b"]
    second_final_r = second_r / len(first)
    second_final_g = second_g / len(first)
    second_final_b = second_b / len(first)
    return (first_final_r, first_final_g, first_final_b, second_final_r, second_final_g, second_final_b)

# putting the average colour into the original pixel grid
def implementAverageColour(originalpixel, average_colours, first, second):
    # contains the average rgb values for first and second lists
    for item in first:
        item["r"] = average_colours[0]
        item["g"] = average_colours[1]
        item["b"] = average_colours[2]
    for item in second:
        item["r"] = average_colours[3]
        item["g"] = average_colours[4]
        item["b"] = average_colours[5]
    for item in first:
        originalpixel[item["x"]][item["y"]] = (item["r"], item["g"], item["b"])
    for item in second:
        originalpixel[item["x"]][item["y"]] = (item["r"], item["g"], item["b"])
    return originalpixel

'''def displayColours():
    fr = average_colours[0]
    fg = average_colours[1]
    fb = average_colours[2]
    sr = average_colours[3]
    sg = average_colours[4]
    sb = average_colours[5]

    display(implementAverageColour(original_list, average_colours, first_list, second_list, fr, fg, fb, sr, sg, sb))'''
