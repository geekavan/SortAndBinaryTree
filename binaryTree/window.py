import numpy as np
import cv2
from Tree import Tree
import sys

background = np.full((600,1100,3),255, np.uint8)
treeStr = sys.argv[1]
orderWay = int(sys.argv[2])
treeList = []
for x in treeStr[1:-1].split(","):
	if x!="None":
		treeList.append(int(x))
	else:
		treeList.append(None)
tree = Tree(background,treeList, 0, 0, 800, 300)
if orderWay==0:
	tree.preorder(tree.nodeList[0])
elif orderWay==1:
	tree.inorder(tree.nodeList[0])
elif orderWay==2:
	tree.postorder(tree.nodeList[0])
else:
	tree.levelorder(tree.nodeList[0])