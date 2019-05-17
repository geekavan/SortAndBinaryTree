from DataSeq import DataSeq
import numpy as np
import cv2
import sys


r = DataSeq("InsertSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)

# 希尔排序
length = len(r.rectangleList)//2
while(length>0):
	for i in range(length, len(r.rectangleList)):
		for j in range(i, -1, -length):
			lengthCopy = 0
			while(i - lengthCopy > -1):
				# 同组的数字设置为绿色
				r.rectangleList[i-lengthCopy].color = (0,255,0)
				lengthCopy = lengthCopy + length
			# 显示
			r.visualize()
			if r.rectangleList[j].value < r.rectangleList[j-length].value:
				r.swap(j, j-length)
			else:
				# 恢复默认色
				lengthCopy = 0
				while(i - lengthCopy > -1):
						r.rectangleList[i-lengthCopy].color = r.rectangleColorDefault
						lengthCopy = lengthCopy + length
				continue
				
		# 恢复默认色
		lengthCopy = 0
		while(i - lengthCopy > -1):
				r.rectangleList[i-lengthCopy].color = r.rectangleColorDefault
				lengthCopy = lengthCopy + length
	length = length//2
		
