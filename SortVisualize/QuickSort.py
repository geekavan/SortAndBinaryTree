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
	pivotValue = array[pivotIndex]
	while rightIndex > leftIndex:
		while rightIndex > leftIndex and array[rightIndex] > pivotValue:
			rightIndex-=1
		while rightIndex > leftIndex and array[leftIndex] <= pivotValue:
			leftIndex+=1
		swap(array, leftIndex, rightIndex)
	swap(array, pivotIndex, rightIndex)
	return rightIndex
	
def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp
	
if __name__ =="__main__":
	r = DataSeq("QuickSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)
	