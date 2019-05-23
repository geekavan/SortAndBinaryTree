import cv2
import numpy as np

'''
设置Node类（即节点类），包含了name，value, leftNode, rightNode, 与在窗口中的圆心，半径， 厚度相关参数属性
为了有更好的显示效果，不建议改动r及thickness的值
'''
class Node():
	def __init__(self, background, value, fatherNode=None, leftNode=None, rightNode=None, xo=0, yo=0, r=15, thickness=2):
		self.__background = background
		self.__value = value
		self.__fatherNode = fatherNode
		self.__leftNode = leftNode
		self.__rightNode = rightNode
		self.__xo = xo
		self.__yo = yo
		self.__r = r
		self.__thickness = thickness
		# 设置背景np.ndarray加上Node（图形表现为一个圆）之后的np.ndarray
		self.__nodeNdarray = cv2.circle(self.__background.copy(), (self.xo, self.yo), self.r, (0,0,0), self.thickness)
		self.__nodeNdarray = cv2.putText(self.__nodeNdarray, str(self.__value), (int(self.__xo-10), int(self.__yo+5)), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0 ,0), 2)
		
	@property
	def value(self):
		return self.__value
		
	@value.setter
	def value(self, value):
		self.__value = value
	
	@property
	def fatherNode(self):
		return self.__fatherNode
		
	@fatherNode.setter
	def fatherNode(self, fatherNode):
		self.__fatherNode = fatherNode
	
	@property
	def leftNode(self):
		return self.__leftNode
		
	@leftNode.setter
	def leftNode(self, leftNode):
		self.__leftNode = leftNode
	
	@property
	def rightNode(self):
		return self.__rightNode
		
	@rightNode.setter
	def rightNode(self, rightNode):
		self.__rightNode = rightNode
		
	@property
	def xo(self):
		return self.__xo
		
	@xo.setter
	def xo(self, xo):
		self.__xo = xo
		
	@property
	def yo(self):
		return self.__yo
		
	@yo.setter
	def yo(self, yo):
		self.__yo = yo
	
	@property
	def r(self):
		return self.__r
		
	@property
	def thickness(self):
		return self.__thickness
		
	@property
	def nodeNdarray(self):
		return self.__nodeNdarray
	# 用于已经排序好的数据染色
	def giveRedColor(self):
		self.__nodeNdarray = cv2.circle(self.__background.copy(), (int(self.xo), int(self.yo)), self.r, (0,0,255), -1)
		# 此中的参数-10和+5是为了看起来有更好的视觉效果而经测试选定的
		self.__nodeNdarray = cv2.putText(self.__nodeNdarray.copy(), str(self.value), (int(self.xo-10), int(self.yo+5)), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 0), 2)
		
	# 用于计算更改xo,yo后的nodeNdarray
	def caculateNodeNdarray(self):
		self.__nodeNdarray = cv2.circle(self.__background.copy(), (int(self.xo), int(self.yo)), self.r, (0,0,0), self.thickness)
		# 此中的参数-10和+5是为了看起来有更好的视觉效果而经测试选定的
		self.__nodeNdarray = cv2.putText(self.__nodeNdarray.copy(), str(self.value), (int(self.xo-10), int(self.yo+5)), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 0), 2)
		
	# 用于node周边的显示
	def ringShow(self, background, title,  time=800):
		ringNdarray = cv2.circle(background.copy(), (int(self.xo),int(self.yo)), self.r+self.thickness, (0,0,255), 5)
		cv2.imshow(title, ringNdarray)
		cv2.waitKey(time)
		return ringNdarray
		
			
	# 用于两个node周边的显示
	def ringShow2(self, Node, background, title,  time=800):
		ringNdarray = cv2.circle(background.copy(), (int(self.xo),int(self.yo)), self.r+self.thickness, (0,0,255), 5)
		ringNdarray = cv2.circle(ringNdarray.copy(), (int(Node.xo),int(Node.yo)), Node.r+Node.thickness, (0,0,255), 5)
		cv2.imshow(title, ringNdarray)
		cv2.waitKey(time)
		return ringNdarray

	# 用于node周边的闪烁
	def flicker(self, background, title, time=200):
		flickerNdarray = cv2.circle(background.copy(), (int(self.xo),int(self.yo)), self.r+self.thickness, (0,0,255), 5)
		for i in range(3):
			cv2.imshow(title, flickerNdarray)
			cv2.waitKey(time)
			cv2.imshow(title, background)
			cv2.waitKey(time)
		return flickerNdarray
			
		
	
			