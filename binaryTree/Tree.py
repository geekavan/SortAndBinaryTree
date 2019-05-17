import cv2
import numpy
from Node import Node
import math
import numpy as np

class Tree():
	def __init__(self, background, treeList, xoFrom, yoFrom, xoTo,  yoTo):
		self.__background = background
		self.__treeList = treeList
		self.__nodeList = self.__getNodeList()
		self.__xoFrom = xoFrom
		self.__yoFrom = yoFrom
		self.__xoTo = xoTo
		self.__yoTo = yoTo
		self.__inputRelation()
		self.__inputXCoordinate(self.__nodeList[0], self.__xoFrom, self.__xoTo)
		self.__inputYCoordinate(self.__yoFrom, self.__yoTo)
		self.__updateNodeNdarray()
		
	@property
	def nodeList(self):
		return self.__nodeList
	
	# 把输入的数字list转变为存储相应值的nodeList,但是如果值为None对应的nodeList也为None
	def __getNodeList(self):
		nodeList = []
		for x in self.__treeList:
			if x:
				nodeList.append(Node(self.__background, x))
			else:
				nodeList.append(None)
		return nodeList

	# 根据输入的treeList，构建各个节点之间的关系
	def __inputRelation(self):
		for i in range(len(self.nodeList)):
			if self.nodeList[i]:
				if (i-1)//2 < 0:
					self.nodeList[i].fatherNode = None
				else:
					self.nodeList[i].fatherNode = self.nodeList[(i-1)//2]
				if (i*2+1) > (len(self.nodeList)-1):
					self.nodeList[i].leftNode = None
				else:
					self.nodeList[i].leftNode = self.nodeList[(i*2+1)]
				if (i*2+2) > (len(self.nodeList)-1):
					self.nodeList[i].rightNode = None
				else:
					self.nodeList[i].rightNode = self.nodeList[(i*2+2)]
			else:
				continue
				
	# 设置每个非空节点的横坐标			
	def __inputXCoordinate(self, root, xoFrom, xoTo):
		if root:
			root.xo = (xoFrom+xoTo)//2
			self.__inputXCoordinate(root.leftNode, xoFrom, root.xo)
			self.__inputXCoordinate(root.rightNode, root.xo, xoTo)
		else:
			return 
	
	# 设置每个非空节点的纵坐标
	def __inputYCoordinate(self, yoFrom, yoTo):
		layer = math.log(len(self.nodeList)+1, 2)
		interval = (yoTo - yoFrom)//layer
		for i in range(len(self.nodeList)):
			if self.nodeList[i]:
				layerNumber = int(math.log(i+1, 2))
				self.nodeList[i].yo = layerNumber*interval+100
			else:
				continue
				
	'''
	经过__inputXCoordinate与__inputYCoordinate过程每个节点的xo与yo值已经改变了，
	但是每个node的nodeNdarray属性还没有改变，此函数用于更新node的nodeNdarray参数
	'''
	def __updateNodeNdarray(self):
		for node in self.nodeList:
				if node:
					node.caculateNodeNdarray()
				else:
					continue

	def getTreeNdarray(self):
		img = np.full(self.__background.shape, 255, np.uint8)
		number = 0
		for node in self.nodeList:
			if node:
				img = img + node.nodeNdarray
				number = number + 1
				if node.fatherNode:
					img = img + self.drawLine(np.full(self.__background.shape, 255, np.uint8), node.xo, node.yo, node.fatherNode.xo, node.fatherNode.yo, node.r)
					number = number + 1
		self.__treeNdarray = img - np.full(self.__background.shape, 255, np.uint8)*number
		return self.__treeNdarray
	
	# 用于两个节点之间画线，该函数也限定了各个节点之间的半径必须是一致的
	def drawLine(self, background, xoFrom, yoFrom, xoTo, yoTo, r):
		cos = (xoTo-xoFrom)/math.sqrt(pow((xoTo-xoFrom), 2)+pow((yoTo-yoFrom), 2))
		sin = (yoTo-yoFrom)/math.sqrt(pow((xoTo-xoFrom), 2)+pow((yoTo-yoFrom), 2))
		pt1x = xoFrom + r*cos
		pt2x = xoTo - r*cos
		pt1y = yoFrom + r*sin
		pt2y = yoTo - r*sin
		return cv2.line(background.copy(), (int(pt1x), int(pt1y)), (int(pt2x), int(pt2y)),(0,0,0), 2)
	
	'''
	前序遍历，使用递归方式
	'''
	def preorder(self, root):
		preorderResult = []
		if not root:
			return preorderResult
		# 只要root不为空，我们都会访问，所以要ringShow一下
		root.ringShow(background = self.getTreeNdarray(), title = "preorder")
		preorderResult.append(root.value)
		# 只要访问了root.value,我们要flicker一下
		root.flicker(background = self.getTreeNdarray(), title = "preorder")
		preorderResult += self.preorder(root.leftNode)
		# if not root.leftNode: 
			# root.fatherNode.ringShow(background = self.getTreeNdarray(), title = "preorder")
		preorderResult +=self.preorder(root.rightNode)
		# if not root.rightNode: 
			# root.fatherNode.ringShow(background = self.getTreeNdarray(), title = "preorder")
		root.fatherNode.ringShow(background = self.getTreeNdarray(), title = "preorder")
		return preorderResult
	'''
	中序遍历，使用递归方式
	'''
	def inorder(self, root):
		inorderResult = []
		if not root:
			return inorderResult
		# 只要root不为空，我们都会访问，所以要ringShow一下
		root.ringShow(background = self.getTreeNdarray(), title = "inorder")
		inorderResult += self.inorder(root.leftNode)
		inorderResult.append(root.value)
		# 只要访问了root.value,我们要flicker一下
		root.flicker(background = self.getTreeNdarray(), title = "inorder")
		inorderResult += self.inorder(root.rightNode)
		# return 都是访问父节点，所以ringShow父节点
		root.fatherNode.ringShow(background = self.getTreeNdarray(), title = "inorder")
		return inorderResult
	
	'''
	后序遍历，使用递归方式
	'''
	def postorder(self, root):
		postorderResult = []
		if not root:
			return postorderResult
		# 只要root不为空，我们都会访问，所以要ringShow一下
		root.ringShow(background = self.getTreeNdarray(), title = "postorder")
		postorderResult += self.postorder(root.leftNode)
		postorderResult += self.postorder(root.rightNode)
		postorderResult.append(root.value)
		# 只要访问了root.value,我们要flicker一下
		root.flicker(background = self.getTreeNdarray(), title = "postorder")
		# return 都是访问父节点，所以ringShow父节点
		root.fatherNode.ringShow(background = self.getTreeNdarray(), title = "postorder")
		return postorderResult