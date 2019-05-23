import numpy as np
import cv2
from TreeForHeapSort import Tree
import sys

background = np.full((600,1100,3),255, np.uint8)
treeStr = sys.argv[1]
treeList = []
for x in treeStr[1:-1].split(","):
	if x!="None":
		treeList.append(int(x))
	else:
		treeList.append(None)
tree = Tree(background,treeList, 0, 0, 800, 300)


def fromTopToBottom(root):
	# 如果root的左右孩子都存在
	if root.leftNode!=None and root.rightNode!=None:
		# 显示两个节点
		root.leftNode.ringShow2(Node = root.rightNode, background = tree.getTreeNdarray(), title="HeapSort")
		if root.leftNode.value < root.rightNode.value:
			tempNode = root.rightNode
		else:
			tempNode = root.leftNode
	elif root.leftNode!=None and root.rightNode==None:
		# 显示唯一子节点
		root.leftNode.ringShow(background = tree.getTreeNdarray(), title="HeapSort")
		tempNode = root.leftNode
	else:
		return
	# 比较具有较大值节点与父节点root大小
	tempNode.ringShow2(Node = root, background = tree.getTreeNdarray(), title="HeapSort")
	if tempNode.value < root.value:
		return
	else:
		temp = root.value
		root.value = tempNode.value
		tempNode.value = temp
		tempNode.caculateNodeNdarray()
		root.caculateNodeNdarray()
		tree.getTreeNdarray()
		# 由于tempNode变动了，以它为根节点的树不一定是最大堆了，所以要调整
		fromTopToBottom(tempNode)
		
def swap(nodeArray, i):
	tempValue = nodeArray[0].value
	nodeArray[0].value = nodeArray[i].value
	nodeArray[i].value = tempValue
	nodeArray[0].caculateNodeNdarray()
	nodeArray[i].caculateNodeNdarray()
	tree.getTreeNdarray()
	if nodeArray[i].fatherNode!=None:
		fatherNode = nodeArray[i].fatherNode
		if fatherNode.leftNode==nodeArray[i]:
			fatherNode.leftNode=None
		else:
			fatherNode.rightNode=None
			
# 把二叉树调整为大根堆
for i in range(len(tree.nodeList)-1, -1, -1):
	fromTopToBottom(tree.nodeList[i])
swap(tree.nodeList, len(tree.nodeList)-1)
tree.nodeList[-1].giveRedColor()
cv2.imshow("HeapSort", tree.getTreeNdarray())
cv2.waitKey(1000)

for i in range(len(tree.nodeList)-1):
	fromTopToBottom(tree.nodeList[0])
	swap(tree.nodeList, len(tree.nodeList)-2-i)
	tree.nodeList[-2-i].giveRedColor()
	cv2.imshow("HeapSort", tree.getTreeNdarray())
	cv2.waitKey(1000)
	
cv2.imshow("HeapSort",tree.getTreeNdarray())
cv2.waitKey(0)
exit()
		
