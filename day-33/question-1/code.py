class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = 0, 0
        n, m = len(version1), len(version2)
        while v1 < n or v2 < m:
            num1, num2 = 0, 0
            while v1 < n and version1[v1] != '.':
                num1 = num1 * 10 + int(version1[v1])
                v1 += 1
            while v2 < m and version2[v2] != '.':
                num2 = num2 * 10 + int(version2[v2])
                v2 += 1
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            v1 += 1
            v2 += 1  
        return 0