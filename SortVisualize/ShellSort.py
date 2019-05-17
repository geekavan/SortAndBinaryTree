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
	for i in range(length, len(r.rectangleList)):
		for j in range(i, length-1, -length):
			# 现在色号储存
			colorj = r.rectangleList[j].color
			colorj_length = r.rectangleList[j-length].color
			# 访问的数组置为红色
			r.rectangleList[j].color = (0,0,255)
			r.rectangleList[j-length].color = (0,0,255)
			# 显示
			r.visualize()
			# 设置为原来的色号
			r.rectangleList[j].color = colorj
			r.rectangleList[j-length].color = colorj_length
			if r.rectangleList[j].value < r.rectangleList[j-length].value:
				r.swapHasNoColorChange(j, j-length)
			else:
				break
	length = length//2
		
