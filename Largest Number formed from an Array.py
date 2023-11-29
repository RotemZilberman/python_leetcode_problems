# User function Template for python3
import functools


class Solution:

    def compare(self, s1, s2):
        for i in range(min(len(s1), len(s2))):
            if s1[i] > s2[i]:
                return 1
            elif s1[i] < s2[i]:
                return -1
        if len(s1) > len(s2):
            if s1[len(s2)] > s2[0]:
                return 1
            elif s1[len(s2)] < s2[0]:
                return -1

        elif len(s1) < len(s2):
            if s2[len(s1)] > s1[0]:
                return -1
            elif s2[len(s1)] < s1[0]:
                return 1
        return 0

    def printLargest(self, arr):
        arr = [str(i) for i in arr]
        arr.sort(key=functools.cmp_to_key(self.compare), reverse=True)
        return "".join(arr)

