#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def diameterHelp(self, root):
        if root is None:
            return 0, 0
        left = self.diameterHelp(root.left)
        right = self.diameterHelp(root.right)
        return max(left[0] + root.data, right[0] + root.data), max(left[0] + right[0] + root.data, left[1], right[1])

    def maxPathSum(self, root):
        return self.diameterHelp(root)[0]

