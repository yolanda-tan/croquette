Croquette is a Python program that converts user provided images into crochet tapestry patterns. It utilises colour quantization to reduce the number of needed colours, and therefore yarn. 

**colour quantization.py and loop.py**

This file contains the functions for quantizing colours; that is, reducing the required colours in the palette to a much smaller number. In this case, under ten colours of yarn as that would be most realistic. Firstly, the image is read in the readImage function, which puts the pixels into a 2D grid of x and y axes. For every pixel, a dictionary is made that stores the r, g, b, values, as well as the original locations via x and y. These dictionaries are then appended into a master list of all pixels in the original image. Then, for each key (r, g, b), the difference between the smallest value and the largest value are computed, then compared against the other keys. The key with the largest difference is the one that the master list is then sorted by. 
This sorted list is then cut down the middle. If more cuts are needed, the program repeats the process of finding the key with the largest difference for each piece. However, this time, the piece with the largest key is the one that is cut. The specified final number of colours minus one is the number of times this process is repeated, ending up with the same number of pieces as desired colours. 
For each piece, the average colour is found by averaging the r, g, b values. After this step, the program replaces the colours in the original list of unmodified pixels with the average colours using the x and y values stored in the dictionaries. 

**pixelate.py**

In pixelate.py, the pixelate function takes in the list of quantized pixels, and final width of the picture in pixels. The middle_selector function is used to maintain the quantized colours. In doing this, the pixelate function returns a list of pixels that matches the desired final width. Each pixel here is now enlarged in the enlarge function for better viewing experience, then a grid is added to differentiate stitches. Finally, the completed image is displayed via the display function. 

**An example**
![image](https://github.com/user-attachments/assets/9ff7c1d0-67e5-4b22-aeb0-af6617fc9f92)
*The above image is the original image*

![image](https://github.com/user-attachments/assets/d23de809-fe84-451f-9e08-546a4fd05ef3)
*The above image is the quantized image (6 colours)*

![image](https://github.com/user-attachments/assets/74c97380-2c97-489e-9178-9c097c3f9c6c)
*The above is the quantized and pixelated image (6 colours)*


![image](https://github.com/user-attachments/assets/a144e47d-c672-4834-b7b2-55e4ec00eeb1)
*The first function will display the quantized picture without pixelation. The second function will display it with pixelation.*
