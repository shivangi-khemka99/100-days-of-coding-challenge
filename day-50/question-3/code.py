class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        bucket = [0]*100

        for i in heights:
            bucket[i-1] +=1
        
        expected = []

        for j in range(len(bucket)):
            for _ in range(bucket[j]):
                expected.append(j+1)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res+=1
        return res        