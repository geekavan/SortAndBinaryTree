import cv2
import numpy as np
from Rectangle import Rectangle


class DataSeq():
	def __init__(self, title, background, dataStr, xoFrom=0, yoFrom=0, xoTo=0,  yoTo=0):
		self.__title = title
		self.__background = background
		self.__dataList = [int(x) for x in dataStr[1:-1].split(",")]
		self.__rectangleColorDefault =(255,0,0)
		self.__rectangleList = [Rectangle(background, x, self.__rectangleColorDefault, 0, (yoFrom+yoTo)//2) for x in self.__dataList]
		self.__xoFrom = xoFrom
		self.__yoFrom = yoFrom
		self.__xoTo = xoTo
		self.__yoTo = yoTo
		# 为了让最左边的柱子不挨着图片边缘图片中而加入横坐标的偏移量shift
		self.__shift = 50
		# 各个柱体之间的间隔
		self.__interval = 20
		self.updateXCoordinate()
	@property
	def title(self):
		return self.__title
	
	@property
	def background(self):
		return self.__background
		
	@property
	def rectangleColorDefault(self):
		return self.__rectangleColorDefault
		
	@property
	def xoFrom(self):
		return self.__xoFrom
		
	@property
	def xoTo(self):
		return self.__xoTo
	
	@property
	def yoTo(self):
		return self.__yoTo
	
	@property
	def shift(self):
		return self.__shift
	
	@property
	def interval(self):
		return self.__interval
		
	@property
	def rectangleList(self):
		return self.__rectangleList
	
	def updateXCoordinate(self):
		if (self.xoFrom+(len(self.rectangleList)-1)*(self.interval + self.rectangleList[0].width) + self.shift) > self.xoTo:
			print("输入数据过多，请减少输入数据的个数")
			exit()
		for i in range(len(self.rectangleList)):
			self.rectangleList[i].xoFrom = self.xoFrom+ i*(self.interval + self.rectangleList[i].width) + self.shift
			# 更新坐标后，重新计算rectangleNdarray
			self.rectangleList[i].updateRectangleNdarray()
			
	def swap(self,i, j):
		# 为正在交换的两个数据设置不一样的颜色
		self.rectangleList[i].color = (0,0,255)
		self.rectangleList[j].color = (0,0,255)
		# 交换rectangleList中的对象位置
		self.rectangleList[i],self.rectangleList[j] = self.rectangleList[j] ,self.rectangleList[i]
		# 重新计算各个rectangle的横坐标
		self.updateXCoordinate()
		# 显示
		self.visualize()
		# 回复原来颜色
		self.rectangleList[i].color = self.__rectangleColorDefault
		self.rectangleList[j].color = self.__rectangleColorDefault
		
	# 用于交换，但交换时并不显示颜色，防止在某些算法中(例如选择排序)显得混乱
	def swapHasNoColorChange(self,i, j):
		# 交换rectangleList中的对象位置
		self.rectangleList[i],self.rectangleList[j] = self.rectangleList[j] ,self.rectangleList[i]
		# 重新计算各个rectangle的横坐标
		self.updateXCoordinate()
		# 显示
		self.visualize()
		
		
	# 用于显示现在的全部self.data
	def visualize(self):
		img = self.background
		for rec in self.rectangleList:
			img = img + rec.rectangleNdarray		
		img = img - self.background * len(self.rectangleList)
		cv2.imshow(self.title, img)
		cv2.waitKey(1000)
		return img
	

