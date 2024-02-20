class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1,x
        res = 0
        while l<=r:
            mid = (l+r)//2
            sq = mid**2
            if sq == x:
                return mid
            elif sq > x:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res,mid)
        return res