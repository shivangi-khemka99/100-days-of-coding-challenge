class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,profit = 0,1,0
        while(r<len(prices)):
            if prices[l] > prices[r]:
                l=r
            else:
                profit = max(profit, prices[r]-prices[l])
            r+=1
        return profit