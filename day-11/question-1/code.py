class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_so_far = 0
        sum_counts = defaultdict(int)
        sum_counts[0] = 1
        
        for num in nums:
            sum_so_far+=num
            diff = sum_so_far-k
            count+=sum_counts[diff]
            sum_counts[sum_so_far]+=1
      
        return count