class Solution(object):
    def findMinMoves(self, machines):
        total = sum(machines)
        if total % len(machines) != 0:
            return -1
        avg = total // len(machines)
        ans = 0
        for i in range(len(machines)):
            ans = max(ans,abs(sum(machines[:i]) - i * avg),abs(sum(machines[:i+1]) - (i+1) * avg))
        return ans
sol = Solution()
print(sol.findMinMoves([0,0,11,5]))