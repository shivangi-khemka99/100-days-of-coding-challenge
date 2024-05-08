import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(max_heap)
        result = [""] * len(score)
        
        for rank in range(1, len(score) + 1):
            _, index = heapq.heappop(max_heap)
            if rank == 1:
                result[index] = "Gold Medal"
            elif rank == 2:
                result[index] = "Silver Medal"
            elif rank == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank)
        return result