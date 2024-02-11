class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count_map = [[] for _ in range(len(nums) + 1)] 

        for i in count:
            count_map[count[i]].append(i)
        
        res = []
        for i in range(len(count_map) - 1, 0, -1):
            for j in count_map[i]:
                res.append(j)
                if len(res) == k:
                    return res