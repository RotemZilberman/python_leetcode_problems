class Solution:
    def diameterHelp(self, root):
        if root is None:
            return None, None
        if root.left is None and root.right is None:
            return root.data, None
        if root.left is None:
            right = self.diameterHelp(root.right)
            return right[0] + root.data, right[1]
        if root.right is None:
            left = self.diameterHelp(root.left)
            return left[0] + root.data, left[1]
        left = self.diameterHelp(root.left)
        right = self.diameterHelp(root.right)
        return max(left[0], right[0]) + root.data, max(left[0] + right[0] + root.data, left[1], right[1])

    def maxPathSum(self, root):
        return self.diameterHelp(root)[1]
