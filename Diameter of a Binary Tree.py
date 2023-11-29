class Solution:

    # Function to return the diameter of a Binary Tree.
    def diameterHelp(self, root):
        if root is None:
            return 0, 0
        left = self.diameterHelp(root.left)
        right = self.diameterHelp(root.right)
        return max(left[0] + 1, right[0] + 1), max(left[0] + right[0] + 2, left[1], right[1])

    def diameter(self, root):
        return self.diameterHelp(root)[1]
