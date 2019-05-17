from DataSeq import DataSeq
import numpy as np
import cv2
import sys


r = DataSeq("BubbleSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)

# 冒泡排序
for i in range(len(r.rectangleList)-1,-1,-1):
	for j in range(0, i):
		# 把访问到的数字置为红色
		r.rectangleList[j].color = (0,0,255)
		r.rectangleList[j+1].color = (0,0,255)
		# 显示
		r.visualize()
		# 恢复原来的色彩
		r.rectangleList[j].color = r.rectangleColorDefault
		r.rectangleList[j+1].color = r.rectangleColorDefault
		if(r.rectangleList[j].value > r.rectangleList[j+1].value):
			r.swap(j, j+1)
	# 把已经排好的设置为绿色
	r.rectangleList[i].color = (0,255,0)