import numpy as np
import cv2 as cv
from PIL import Image
import sys#for printing whole array for debugging
np.set_printoptions(threshold=sys.maxsize)
# from matplotlib import pyplot as plt
def getsize(filename):
	# print("1")
	image1 = cv.imread(filename)
	#at white background and also black backgorund for other parameters have to change======================
	gray = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
	ret, thresh = cv.threshold(gray, 75, 255, cv.THRESH_BINARY)
	image1[thresh == 255] = 0
	# imS = cv.resize(image1, (960, 940))
	cv.imshow('boundaery image',image1)
	cv.destroyAllWindows()
	# print("2")
	# =============================change colour image to gray image======================================================
	image1gray = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
	# imS = cv.resize(image1gray, (960, 940))
	cv.imshow('boundaery image',image1gray)
	cv.destroyAllWindows()
	#=========================changing gray image to binary for time efficiency================================================================
	#===If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value===========
	#its input 1 argument is source Image,2nd is threshold pixel ,3rd is maximum pixel,4th is type of thresholding
	#its output 1st argument is thresholding value use ie.. 2nd argument of imput
	ret, thresh = cv.threshold(image1gray, 45, 255, 0)
	#=====================finding contours=================================
	contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	# print(contours)
	# print(contours)
	largest_contour = []
	largest_area = 0
	i=0;
	for contour in contours:
	    # print(i)
	    # i=i+1
	    area = cv.contourArea(contour)
	    if area > largest_area:
	        largest_area = area
	        largest_contour = contour


	# image2 = cv.imread('red_apple.jp0g')
	image2 = cv.imread('red_apple.jpg')
	# imS = cv.resize(image2, (960, 940))
	start_x,start_y,width,height = cv.boundingRect(largest_contour)
	# print(start_x,start_y,width,height)
	# print("area of apple is ",width*height)
	var=-1;
	if ((width*height)<=32000):
	    var="SMALL"
	else:
	    var="BIG"

	# print(largest_contour,largest_area)
	# cv.drawContours(image2, [largest_contour], -1, (255, 255, 255), 3)
	# cv.rectangle(image2, (start_x,start_y), (start_x+width, start_y+height), (255, 255, 255), 2)
	# # imS = cv.resize(image2, (960, 940))
	# cv.imshow('boundaery image',image2)
	# cv.destroyAllWindows()
	# image2 = cv.cvtColor(image2, cv.COLOR_BGR2RGB)
	# image2=Image.fromarray((image2).astype(np.uint8))
	# image2.save('out.jpg')
	return var