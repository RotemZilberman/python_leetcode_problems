class Solution:
    arr1 = []
    len1 = 0
    arr2 = []
    len2 = 0
    def inorder(self, root, id):
        if root is None:
            return
        self.inorder(root.left, id)
        if id == 1:
            self.arr1.append(root.data)
            self.len1 += 1
        else:
            self.arr2.append(root.data)
            self.len2 += 1
        self.inorder(root.right, id)

    def merge(self, root1, root2):
        self.inorder(root1, 1)
        self.inorder(root2, 2)
        i = 0
        j = 0
        arr = []
        while i < self.len1 and j < self.len2:
            if self.arr1[i] < self.arr2[j]:
                arr.append(self.arr1[i])
                i += 1
            else:
                arr.append(self.arr2[j])
                j += 1
        while i < self.len1:
            arr.append(self.arr1[i])
            i += 1
        while j < self.len2:
            arr.append(self.arr2[j])
            j += 1
        return arr