import cv2
from DataSeq import DataSeq
from Rectangle import Rectangle
import numpy as np
import sys

r = DataSeq("MergeSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)
def mergeSort(array):
	return divide(array)
		
def divide(array):
	mid = len(array)//2
	if mid==0 or mid==len(array):
		return array
	leftList = array[0:mid]
	rightList = array[mid:len(array)]
	leftList = divide(leftList)
	rightList = divide(rightList)
	return conquer(leftList, rightList)
	
def conquer(leftList, rightList):
	# 记录要比较的两个数组中每个rectangle的位置
	position = []
	for i in leftList:
		position.append((i.xoFrom, i.yoFrom))
	for i in rightList:
		position.append((i.xoFrom, i.yoFrom))
	# 将正在进行比较的数字设置为红色
	for i in leftList:
		i.color = (0,0,255)
	for i in rightList:
		i.color = (0,0,255)
	#显示
	r.visualize()
	# 用于记录已经排好了num个数据
	num = 0
	img = r.visualize()
	result = []
	while len(leftList) and len(rightList):
		if leftList[0].value < rightList[0].value:
			# 在窗口下方显示已经比较好的数据
			img = img + Rectangle(r.background, leftList[0].value, (255, 0, 0), num * (r.interval + leftList[0].width) + r.shift, r.yoTo).rectangleNdarray
			img = img - r.background
			cv2.imshow(r.title, img)
			cv2.waitKey(1000)
			result.append(leftList.pop(0))
		else:
			# 在窗口下方显示已经比较好的数据
			img = img + Rectangle(r.background, rightList[0].value, (255, 0, 0), num * (r.interval + rightList[0].width) + r.shift, r.yoTo).rectangleNdarray
			img = img - r.background
			cv2.imshow(r.title, img)
			cv2.waitKey(1000)
			result.append(rightList.pop(0))
		num = num + 1
	while len(leftList):
		# 在窗口下方显示已经比较好的数据
		img = img + Rectangle(r.background, leftList[0].value, (255, 0, 0), num * (r.interval + leftList[0].width) + r.shift, r.yoTo).rectangleNdarray
		img = img - r.background
		cv2.imshow(r.title, img)
		cv2.waitKey(1000)
		result.append(leftList.pop(0))
		num = num + 1
	while len(rightList):
		# 在窗口下方显示已经比较好的数据
		img = img + Rectangle(r.background, rightList[0].value, (255, 0, 0), num * (r.interval + rightList[0].width) + r.shift, r.yoTo).rectangleNdarray
		img = img - r.background
		cv2.imshow(r.title, img)
		cv2.waitKey(1000)
		result.append(rightList.pop(0))
		num = num + 1
	print([x.value for x in result])
	# 恢复蓝色
	for i in range(len(result)):
		result[i].color = r.rectangleColorDefault
		result[i].xoFrom = position[i][0]
		result[i].yoFrom = position[i][1]
	#显示
	r.visualize()
	return result
	
if __name__=="__main__":
	r = DataSeq("MergeSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)
	print([x.value for x in mergeSort(r.rectangleList)])