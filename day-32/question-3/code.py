import sys
sys.set_int_max_str_digits(100000)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for nums in num:
            while stack and k>0 and nums<stack[-1]:
                k-=1
                stack.pop()
            stack.append(nums)
        stack = stack[:len(stack)-k]
        res = "".join(stack)
        return str(int(res)) if res else "0"