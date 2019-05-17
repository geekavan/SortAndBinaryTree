# tkinter为python的GUI库
import tkinter as tk
import os

# 创建tkinter.Tk对象，名字为window实际上就是窗口对象
window = tk.Tk()
# 窗口上显示的名字
window.title("my graduate work")
# 窗口的大小
window.geometry("970x600")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 排序部分开始
def  bubbleSort():
	os.system("python ./jobSort/bubbleSort.py")
	
def  selectSort():
	os.system("python ./jobSort/selectSort.py")
	
def  insertSort():
	os.system("python ./jobSort/insertSort.py")
	
def  shellSort():
	os.system("python ./jobSort/shellSort.py")

def  mergeSort():
	os.system("python ./jobSort/mergeSort.py")
	
def  quickSort():
	os.system("python ./jobSort/quickSort.py")
	
def  heapSort():
	os.system("python ./jobSort/heapSort.py")

# 用于设定各个排序算法按钮的坐标，他们之间的间隔通过interval设置
def sortOptionPosition(xStartPosition = 50, yStratPosition = 100, interval = 70):
	positionList = []
	for i in range(7):
		positionList.append((xStartPosition, int(yStratPosition+i*interval)))
	return positionList

positionList = sortOptionPosition()

buttonForBubbleSort = tk.Button(window, text='BubbleSort',font=('Arial', 12), width=13, height=2, command=bubbleSort)
buttonForBubbleSort.place(x = positionList[0][0],y=positionList[0][1])

buttonForSelectSort = tk.Button(window, text='SelectSort',font=('Arial', 12), width=13, height=2, command=selectSort)
buttonForSelectSort.place(x=positionList[0][0],y=positionList[1][1])

buttonForInsertSort = tk.Button(window, text='InsertSort',font=('Arial', 12), width=13, height=2, command=insertSort)
buttonForInsertSort.place(x=positionList[0][0],y=positionList[2][1])

buttonForShellSort = tk.Button(window, text='ShellSort',font=('Arial', 12), width=13, height=2, command=shellSort)
buttonForShellSort.place(x=positionList[0][0],y=positionList[3][1])

buttonForMergeSort = tk.Button(window, text='MergeSort',font=('Arial', 12), width=13, height=2, command=mergeSort)
buttonForMergeSort.place(x=positionList[0][0],y=positionList[4][1])

buttonForQuickSort = tk.Button(window, text='QuickSort',font=('Arial', 12), width=13, height=2, command=quickSort)
buttonForQuickSort.place(x=positionList[0][0],y=positionList[5][1])

buttonForHeapSort = tk.Button(window, text='HeapSort',font=('Arial', 12), width=13, height=2, command=heapSort)
buttonForHeapSort.place(x=positionList[0][0],y=positionList[6][1])
# 排序部分结束
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 二叉树部分开始
def treeTraversal():
	os.system("python ./BinaryTree/window.py" + " " + entryForTreeStr.get() + " " + str(v.get()))
	return 
# 建立输入框对象，用于输入二叉树string
entryForTreeStr = tk.Entry(window,width = 70)
entryForTreeStr.insert('end',"[11,28,37,41,52,63,None,None,77,45,None,15,None,None,None]")
entryForTreeStr.place(x = 300, y = 100)
# 建立单选框，用于选择二叉树的遍历方式
v = tk.IntVar()
v.set(0)
radiobuttonForTraversalWayPreorder =tk.Radiobutton(window,variable = v,text = 'preorder',value = 0).place(x=300, y = 160)
radiobuttonForTraversalWayInorder =tk.Radiobutton(window,variable = v,text = 'inorder',value = 1).place(x=300, y = 230)
radiobuttonForTraversalWayPostorder =tk.Radiobutton(window,variable = v,text = 'postorder',value = 2).place(x=300, y = 300)
radiobuttonForTraversalWayLevelorder =tk.Radiobutton(window,variable = v,text = 'levelorder',value = 3).place(x=300, y = 370)
# 建立按钮，用于确认二叉树的相关输入
buttonForTreeInputConfirm = tk.Button(window, text='Confirm',font=('Arial', 12), width=13, height=2, command=treeTraversal)
buttonForTreeInputConfirm.place(x=300, y = 450)
# 二叉树部分结束
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 可自定义输入排序部分开始
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def bubbleSort2():
	os.system("python ./SortVisualize/BubbleSort.py" + " " + entryForSortStr.get())

def selectSort2():
	os.system("python ./SortVisualize/SelectSort.py" + " " + entryForSortStr.get())

def insertSort2():
	os.system("python ./SortVisualize/InsertSort.py" + " " + entryForSortStr.get())

def shellSort2():
	os.system("python ./SortVisualize/ShellSort.py" + " " + entryForSortStr.get())
	
# 建立输入框对象，用于输入排序string
entryForSortStr = tk.Entry(window,width = 60)
entryForSortStr.insert('end',"[5,9,4,3,10,6,8,7,1,2,11]")
entryForSortStr.place(x = 500, y = 150)


buttonForBubbleSort2 = tk.Button(window, text='BubbleSort',font=('Arial', 12), width=13, height=2, command=bubbleSort2)
buttonForBubbleSort2.place(x = 500,y=190)

buttonForSelectSort2 = tk.Button(window, text='SelectSort',font=('Arial', 12), width=13, height=2, command=selectSort2)
buttonForSelectSort2.place(x = 500,y=250)

buttonForInsertSort2 = tk.Button(window, text='InsertSort',font=('Arial', 12), width=13, height=2, command=insertSort2)
buttonForInsertSort2.place(x = 500,y=310)

buttonForShellSort2 = tk.Button(window, text='ShellSort',font=('Arial', 12), width=13, height=2, command=shellSort2)
buttonForShellSort2.place(x = 500,y=370)

window.mainloop()