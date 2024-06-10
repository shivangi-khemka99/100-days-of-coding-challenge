class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first,first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i != minH[0]:
                        return False
                    else:
                        heapq.heappop(minH)
        return True