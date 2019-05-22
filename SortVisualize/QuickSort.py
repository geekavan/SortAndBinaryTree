import cv2
from DataSeq import DataSeq
from Rectangle import Rectangle
import numpy as np
import sys


def quickSort(array):
	devide(array, 0, len(array)-1)
	return array
	
def devide(array, leftIndex, rightIndex):
	if leftIndex >= rightIndex:
		return
	pivotIndex = conquer(array, leftIndex, rightIndex)
	devide(array, leftIndex, pivotIndex-1)
	devide(array, pivotIndex+1, rightIndex)
	
def conquer(array, leftIndex, rightIndex):
	pivotIndex = leftIndex
	pivotValue = array[pivotIndex].value
	# 将基准设置为绿色，右指针数据设置为红色
	array[pivotIndex].color = (0,255,0)
	array[rightIndex].color = (0,0,255)
	# 显示
	r.visualize()
	while rightIndex > leftIndex:
		while rightIndex > leftIndex and array[rightIndex].value > pivotValue:
			if rightIndex==pivotIndex:
				pass
			else:
				# 先前指针数据恢复原色
				array[rightIndex].color = r.rectangleColorDefault
			rightIndex-=1
			# 现在指针数据设置为红色
			array[rightIndex].color = (0,0,255)
			# 显示
			r.visualize()
		while rightIndex > leftIndex and array[leftIndex].value <= pivotValue:
			if leftIndex==pivotIndex:
				pass
			else:
				# 先前指针数据恢复原色	
				array[leftIndex].color = r.rectangleColorDefault
			leftIndex+=1
			# 现在指针数据设置为红色
			array[leftIndex].color = (0,0,255)
			# 显示
			r.visualize()
		r.swapHasNoColorChange(leftIndex, rightIndex)
	if leftIndex==pivotIndex:
		array[leftIndex].color = (0,255,0)
	else:
		# 最后的指针数据恢复原色
		array[leftIndex].color = r.rectangleColorDefault
	r.swapHasNoColorChange(pivotIndex, rightIndex)
	return rightIndex
	
	
if __name__ =="__main__":
	r = DataSeq("QuickSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)
	quickSort(r.rectangleList)
	
	