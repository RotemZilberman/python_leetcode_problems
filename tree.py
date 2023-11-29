
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def scanTree(self, root, ls):
        if root == None:
            return
        if root.left == None and root.right == None:
            ls.append(root.data)
            return
        self.scanTree(root.left, ls)
        self.scanTree(root.right, ls)

    def printBoundaryView(self, root):
        list = []
        temp = root
        while True:
            if temp.left is None and temp.right is None:
                break
            if temp.left is not None:
                list.append(temp.data)
                temp = temp.left
            elif temp.right is not None:
                list.append(temp.data)
                temp = temp.right
        temp = root
        self.scanTree(root, list)
        ls2 = []
        while True:
            if temp.left is None and temp.right is None:
                break
            if temp.right is not None:
                list.append(temp.data)
                temp = temp.right
            elif temp.left is not None:
                list.append(temp.data)
                temp = temp.left
        ls2.reverse()
        list.extend(ls2)
        return list