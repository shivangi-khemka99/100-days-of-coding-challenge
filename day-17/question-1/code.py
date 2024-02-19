class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1, n
        res = 0
        while(l<=r):
            mid = (l+r) // 2
            summ = (mid / 2) * (mid+1)
            if summ > n :
                r = mid - 1 
            else:
                l = mid + 1
                res = max(mid, res)
        return res