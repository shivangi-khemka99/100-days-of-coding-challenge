class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sum_so_far = 0
        prefix_sum = defaultdict(int) 
        prefix_sum[0] = 1
        for num in nums:
            sum_so_far += num
            rem = sum_so_far % k 
            count += prefix_sum[rem]
            prefix_sum[sum_so_far%k] += 1
        return count