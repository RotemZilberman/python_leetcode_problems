class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        j=0
        w=0
        ans=[]
        if len(nums1) + len(nums2) <= k:
            for i in range(len(nums1)+len(nums2)):
                if nums1[j] > nums2[w]:
                    ans.append(nums1[j])
                    j+=1
                else:
                    ans.append(nums2[w])
                    w+=1
            return ans
        while len(ans) < k:
            MaxNums1 = 0
            maxIndex1 = 0
            MaxNums2 = 0
            maxIndex2 = 0
            for i in range(j,k - len(nums2) + w + 1):
                if nums1[i] > MaxNums1:
                    MaxNums1 = nums1[i]
                    maxIndex1 = i
            for i in range(w,k - len(nums1) + j + 1):
                if nums2[i] > MaxNums2:
                    MaxNums2 = nums2[i]
                    maxIndex2 = i
            if MaxNums1 > MaxNums2:
                ans.append(MaxNums1)
                j = maxIndex1 + 1
            else:
                ans.append(MaxNums2)
                w = maxIndex2 + 1
