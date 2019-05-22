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
	# 将左右指针数据设置为红色
	array[leftIndex].color = (0,0,255)
	array[rightIndex].color = (0,0,255)
	# 显示
	r.visualize()
	while rightIndex > leftIndex:
		while rightIndex > leftIndex and array[rightIndex].value > pivotValue:
			# 先前指针数据恢复原色
			array[rightIndex].color = r.rectangleColorDefault
			rightIndex-=1
			# 现在指针数据设置为红色
			array[rightIndex].color = (0,0,255)
			# 显示
			r.visualize()
		while rightIndex > leftIndex and array[leftIndex].value <= pivotValue:
			# 先前指针数据恢复原色	
			array[leftIndex].color = r.rectangleColorDefault
			leftIndex+=1
			# 现在指针数据设置为红色
			array[leftIndex].color = (0,0,255)
			# 显示
			r.visualize()
		r.swapHasNoColorChange(leftIndex, rightIndex)
		# swap(array, leftIndex, rightIndex)
	# swap(array, pivotIndex, rightIndex)
	r.swapHasNoColorChange(pivotIndex, rightIndex)
	return rightIndex
	
def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp
	
if __name__ =="__main__":
	r = DataSeq("QuickSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)
	# print([x.value for x in quickSort(r.rectangleList)])
	quickSort(r.rectangleList)
	
	