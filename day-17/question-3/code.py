class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1,num
        res = 1
        while (l<=r):
            mid = (l+r) // 2
            sq = mid ** 2
            if sq > num:
                r = mid - 1
            elif sq < num:
                l = mid + 1
            else:
                return True
        return False