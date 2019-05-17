from DataSeq import DataSeq
import numpy as np
import cv2
import sys


r = DataSeq("InsertSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)

# 希尔排序
length = len(r.rectangleList)//2
# 自己设定的色盘
colorList = [(0,255,0),(255,255,0),(255,0,255),(0,255,255),(127,127,0),(127,0,127),(0,127,127),(127,127,255),(127,255,127),(255,127,127),(64,64,127),(64,127,64),(127,64,64),(32,32,255),(32,255,32),(255,32,32)]
		
while length > 0:
	# 同组的进行染色
	for i in range(length):
		j = i
		while(j < len(r.rectangleList)):
			r.rectangleList[j].color = colorList[i]
			j = j + length
	r.visualize()
	for i in range(length, len(r.rectangleList)):
		for j in range(i, length-1, -length):
			if r.rectangleList[j].value < r.rectangleList[j-length].value:
				r.swapHasNoColorChange(j, j-length)
				r.visualize()
				r.visualize()
			else:
				break
	length = length//2
		
