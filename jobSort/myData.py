import random
import numpy as np
import time
import cv2


class DataSeq:
	# 先定义好各个颜色的三原色参数值，后边直接调用如self.WHITE
	# (蓝色参数，绿色参数， 红色参数)
    WHITE = (255,255,255)
    RED = (0,0,255)
    BLACK = (0,0,0)
    YELLOW = (0,127,255)
	
    MAX_IM_SIZE = 500
    def __init__(self, Length, time_interval=1, 
                                sort_title="Figure"):
        self.data = [x for x in range(Length)]
		# 随机打乱
        self.Shuffle()
        self.length = Length

		# 把参数time_interval赋值给成员变量self.time_interval
        self.SetTimeInterval(time_interval)
		# 把参数sort_title赋值给成员变量self.sort_title
        self.SetSortType(sort_title)
        self.Getfigure()
		# 初始化时间
        self.InitTime()
        self.Visualize()

    def InitTime(self):
	# 计算当前时间戳，时间戳为从1970年1月1日00：00：00开始按秒计算的偏移量
        self.start=time.time()
        self.time=0
        self.StopTimer()

    def StartTimer(self):
        self.start_flag=True
        self.start = time.time()

    def StopTimer(self):
        self.start_flag=False

    def GetTime(self):
	# 如果self.start_flag为真，计算从执行self.start到现在的秒偏移数
        if self.start_flag:
            self.time = time.time()-self.start

    def SetTimeInterval(self, time_interval):
        self.time_interval=time_interval

    def SetSortType(self, sort_title):
        self.sort_title=sort_title

    def Shuffle(self):
	# 打乱self.data的顺序
        random.shuffle(self.data)

    def Getfigure(self):
        _bar_width = 5
		# 这是图片的numpy.ndarray,最后一维为3维，为颜色的维数
        figure = np.full((self.length*_bar_width,self.length*_bar_width,3), 255,dtype=np.uint8)
        for i in range(self.length):
            val = self.data[i]
			# 因为各个数据柱子是紧紧挨着的，所以为了有区分度给相邻的各个数据柱子赋予不同的颜色
            figure[-1-val*_bar_width:, i*_bar_width:i*_bar_width+_bar_width] = self.GetColor(val, self.length)
        self._bar_width = _bar_width
        self.figure = figure
        size = _bar_width*self.length
        self.im_size = size if size < self.MAX_IM_SIZE else self.MAX_IM_SIZE

    @staticmethod
    def GetColor(val, TOTAL):
		# 给不同的数据柱子赋予不同的颜色
        return (120+val*255//(2*TOTAL), 255-val*255//(2*TOTAL), 0)

    def _set_figure(self, idx, val):
        min_col = idx*self._bar_width
        max_col = min_col+self._bar_width
        min_row = -1-val*self._bar_width
        self.figure[ : , min_col:max_col] = self.WHITE
        self.figure[ min_row: , min_col:max_col] = self.GetColor(val, self.length)

    def SetColor(self, img, marks, color):
        for idx in marks:
            min_col = idx*self._bar_width
            max_col = min_col+self._bar_width
            min_row = -1-self.data[idx]*self._bar_width
            img[min_row:, min_col:max_col] = color
    def Mark(self, img, marks, color):
        self.SetColor(img, marks, color)
		
    def SetVal(self, idx, val):
        self.data[idx] = val
        self._set_figure(idx, val)

        self.Visualize((idx,))
		# 交换self.data中index为idx1与idx2的数据
    def Swap(self, idx1, idx2):
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        self._set_figure(idx1, self.data[idx1])
        self._set_figure(idx2, self.data[idx2])

        self.Visualize((idx1, idx2))

    def Visualize(self, mark1=None, mark2=None):
        img = self.figure.copy()
        if mark2:
            self.Mark( img, mark2, self.YELLOW)
        if mark1:
            self.Mark( img, mark1, self.RED)
		# 重新设置img的大小
        img = cv2.resize(img, (self.im_size, self.im_size))
        # 计算程序执行到现在所用的时间，赋值给self.time
        self.GetTime()
		# 在图像img上设置文字（现在的时间），文字的位置，字体，大小，颜色和粗细
        cv2.putText(img, self.sort_title+" Time:%02.2fs"%self.time, (20,20), cv2.FONT_HERSHEY_PLAIN, 1, self.YELLOW, 1)

		# 显示图像img及图像的标题self.sort_title
        cv2.imshow(self.sort_title, img)
		# 出现self.time_interval才关闭图像
        cv2.waitKey(self.time_interval)