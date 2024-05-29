class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l,r = 0,0
        summ,res = 0,0
        while l<len(s) and r<len(s):
            if summ + abs(ord(s[r]) - ord(t[r])) <= maxCost:
                summ += abs(ord(s[r]) - ord(t[r]))
                r+=1
            else:
                summ -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            res = max(res,r-l)
        return res