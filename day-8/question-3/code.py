class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1,num2 = set(nums1), set(nums2)
        res1, res2 = set(), set()
        for i in nums1:
            if i not in num2:
                res1.add(i)
        for i in nums2:
            if i not in num1:
                res2.add(i)
        return [list(res1), list(res2)]
    

# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         set1 = set(nums1)
#         set2 = set(nums2)
        
#         diff1 = set1 - set2
#         diff2 = set2 - set1
        
#         return [list(diff1), list(diff2)]