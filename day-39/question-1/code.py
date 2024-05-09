class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        max_sum,j = 0,len(happiness)-1
        for i in range(k):
            if happiness[j]-i>0:
                max_sum+=(happiness[j]-i)
            else:
                break
            j-=1
        return max_sum