class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a,b,last = m-1, n-1, m+n-1

        while a>=0 and b>=0:
            if nums1[a] > nums2[b]:
                nums1[last] = nums1[a]
                a-=1
            else:
                nums1[last] = nums2[b]
                b-=1
            last-=1
            
        while b >= 0:
            nums1[last] = nums2[b]
            b-=1
            last-=1