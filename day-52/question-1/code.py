class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # square_root = set()
        # for i in range(int(sqrt(c))+1):
        #     square_root.add(i*i)
        # a = 0
        # while a*a <= c:
        #     target = c - a*a
        #     if target in square_root:
        #         return True
        #     a +=1
        # return False

        left,right = 0, int(sqrt(c))
        while left<=right:
            total = left*left + right*right
            if total == c:
                return True
            elif total > c:
                right-=1
            else:
                left+=1
        return False