import cv2

class Rectangle():
	def __init__(self, background, value, color=(255,0,0), xoFrom=0, yoFrom=0):
		self.__background = background
		self.__value = value
		self.__color = color
		self.__xoFrom = xoFrom
		self.__yoFrom = yoFrom
		# width为矩形的宽度，为了有较好的视觉效果，这里选定为20不可改动
		self.__width = 20
		rectangleNdarray = cv2.rectangle(background.copy(), (int(xoFrom), int(yoFrom)),(int(xoFrom+self.__width), int(yoFrom-value*10)),color, -1)
		rectangleNdarray = cv2.putText(rectangleNdarray.copy(), str(value), (xoFrom, yoFrom-5), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 0), 2)
		self.__rectangleNdarray = rectangleNdarray
	
	@property
	def value(self):
		return self.__value
		
	@property
	def background(self):
		return self.__background
		
	@property
	def color(self):
		return self.__color
		
	@color.setter
	def color(self, color):
		self.__color = color
		self.updateRectangleNdarray()
	
	@property
	def xoFrom(self):
		return self.__xoFrom
		
	@xoFrom.setter
	def xoFrom(self, xoFrom):
		self.__xoFrom = xoFrom
		self.updateRectangleNdarray()
		
	@property
	def yoFrom(self):
		return self.__yoFrom
		
	@yoFrom.setter
	def yoFrom(self, yoFrom):
		self.__yoFrom = yoFrom
		
	@property
	def width(self):
		return self.__width
	
	@property
	def rectangleNdarray(self):
		return self.__rectangleNdarray
		
	def updateRectangleNdarray(self):
		rectangleNdarray = cv2.rectangle(self.background.copy(), (int(self.xoFrom), int(self.yoFrom)),(int(self.xoFrom+self.width), int(self.yoFrom-self.value*10)),self.color, -1)
		rectangleNdarray = cv2.putText(rectangleNdarray.copy(), str(self.value), (self.xoFrom, self.yoFrom-5), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 0), 2)
		self.__rectangleNdarray = rectangleNdarray
		
	
		