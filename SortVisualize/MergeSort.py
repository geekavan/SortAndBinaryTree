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
	rectangle = 
	result = []
	while len(leftList) and len(rightList):
		if leftList[0].value < rightList[0].value:
			result.append(leftList.pop(0))
		else:
			result.append(rightList.pop(0))
	while len(leftList):
		result.append(leftList.pop(0))
	while len(rightList):
		result.append(rightList.pop(0))
	print([x.value for x in result])
	return result
	
if __name__=="__main__":
	r = DataSeq("MergeSort", np.full((600,1100,3),255, np.uint8),sys.argv[1], 0,0,1100,600)
	print([x.value for x in mergeSort(r.rectangleList)])