from DataSeq import DataSeq
import numpy as np
import cv2
import sys


r = DataSeq("SelectSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)

# 选择排序
for i in range(len(r.rectangleList)):
	minIndex = i
	for j in range(i, len(r.rectangleList)):
		# 把访问到的数字置为红色
		r.rectangleList[j].color = (0,0,255)
		# 显示
		r.visualize()
		# 恢复为默认色
		r.rectangleList[j].color = r.rectangleColorDefault
		# 将目前最小的数设置为黄色
		r.rectangleList[minIndex].color= (0,0,255)
		# 显示
		# r.visualize()
		if r.rectangleList[j].value < r.rectangleList[minIndex].value:
			# 如果出现了更小的数把原来的数字设置为默认色，新的最小数字设置为黄色
			r.rectangleList[minIndex].color = r.rectangleColorDefault
			minIndex = j
			r.rectangleList[minIndex].color = (0,0,255)
	# 交换最小数字与当前在i上的数字
	r.swapHasNoColorChange(i, minIndex)
	# 将已经排好序的数字设置为绿色
	r.rectangleList[i].color = (0,255,0)
	# r.visualize()
			
		
