class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        minHeap,n = [],len(arr)
        for i in range(n - 1):
            heapq.heappush(minHeap, (arr[i] / arr[-1], i, n - 1))

        for _ in range(k - 1):
            _, numeratorIndex, denominatorIndex = heapq.heappop(minHeap)
            if denominatorIndex - 1 > numeratorIndex:
                heapq.heappush(
                    minHeap, (arr[numeratorIndex] / arr[denominatorIndex - 1], numeratorIndex, denominatorIndex - 1))

        _, i, j = heapq.heappop(minHeap)
        return [arr[i], arr[j]]