class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []
        for val in arr2:
            result.extend([val] * count.pop(val, 0))
        remaining = sorted(count.elements())
        result.extend(remaining)
        return result