from DataSeq import DataSeq
import numpy as np
import cv2
import sys


r = DataSeq("InsertSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)

# 插入排序
for i in range(len(r.rectangleList)):
	for j in range(i, 0, -1):
		# 访问的数字设置为红色
		r.rectangleList[j].color = (0,0,255)
		r.rectangleList[j-1].color = (0,0,255)
		# 显示
		r.visualize()
		# 恢复默认色
		r.rectangleList[j].color = r.rectangleColorDefault
		r.rectangleList[j-1].color = r.rectangleColorDefault
		if r.rectangleList[j].value < r.rectangleList[j-1].value:
			r.swap(j, j-1)
		else:
			continue			
		
