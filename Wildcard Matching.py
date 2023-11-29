class Solution(object):
    def isMatch(self, s, p):
        startP = 0
        EndP = 0
        kSeq = 0
        while kSeq < len(p):
            if p[startP] != '*':
                if p[startP] == s[kSeq] or p[startP] == '?':
                    startP += 1
                    kSeq += 1
                else:
                    return False
            else:
                EndP = startP
                while EndP < len(p) and p[EndP] == '*':
                    EndP += 1
                if EndP == len(p):
                    back = kSeq
                    kSeq = len(s)-1
                    while kSeq >= back and EndP >= startP:
                        if s[kSeq] != p[EndP-1] and p[EndP-1] != '?':
                            return False
                        kSeq -= 1
                        EndP -= 1
                    if kSeq < back:
                        return False
                    return True
                else:
                    back = kSeq
                    kSeq = len(s)-1
                    while kSeq >= back and EndP >= startP:
                        if s[kSeq] != p[EndP-1] and p[EndP-1] != '?':
                            return False
                        kSeq -= 1
                        EndP -= 1
                    if kSeq < back:
                        return False
                    startP = EndP
        if kSeq < len(s):
            return False
        return True
sol = Solution()
print(sol.isMatch("aa","*"))