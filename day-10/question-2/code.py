class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_length = 0
        
        for num in hashset:
            if num - 1 not in hashset:  # Only start from the smallest number of a sequence
                current_num = num
                current_length = 1
                
                # Count consecutive numbers from the current number
                while current_num + 1 in hashset:
                    current_num += 1
                    current_length += 1
                
                # Update the maximum length
                max_length = max(max_length, current_length)
        
        return max_length