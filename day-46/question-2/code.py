#TIME COMPLEXITY : O(N*2^N)
# class Solution:
#     def check_if_beautiful(self, arr, k):
#         check = set()
#         for i in arr:
#             if i + k in check or (i - k) in check:
#                 return False
#             check.add(i)
#         return True

#     def beautifulSubsets(self, nums: List[int], k: int) -> int:
#         res = 0
#         part = []
#         def helper(i):
#             nonlocal res
#             if i >= len(nums):
#                 if part:
#                     res += 1
#                 return
#             #Include nums[i]
#             part.append(nums[i])
#             if self.check_if_beautiful(part,k):
#                 helper(i+1)
#             #Exclude nums[i]
#             part.pop()
#             if self.check_if_beautiful(part,k):
#                 helper(i+1)
#         helper(0)
#         return res

#TIME COMPLEXITY : O(2^N)

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def helper(i, part):
            nonlocal res
            if i >= len(nums):
                res += 1
                return
            # Include nums[i]
            if not (nums[i] + k in part or nums[i] - k in part):
                part[nums[i]] = part.get(nums[i], 0) + 1
                helper(i + 1, part)
                part[nums[i]] -= 1
                if part[nums[i]] == 0:
                    del part[nums[i]]
            # Exclude nums[i]
            helper(i + 1, part)

        res = 0
        helper(0, {})
        return res-1
