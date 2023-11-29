import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2.0
        if len(nums1) == 0 and len(nums2) == 1:
            return nums2[0]
        if len(nums2) == 0 and len(nums1) == 1:
            return nums1[0]
        if nums1[int(len(nums1) / 2)] > nums2[int(len(nums2) / 2)]:
            return self.findMedianSortedArrays(nums1[:int(math.ceil(len(nums1) / 2))], nums2[int(math.floor(len(nums2) / 2)):])
        else:
            return self.findMedianSortedArrays(nums1[int(math.floor(len(nums1) / 2)):], nums2[:int(math.ceil(len(nums2) / 2))])

sul = Solution()
print(sul.findMedianSortedArrays([1, 2], [3, 4, 5]))