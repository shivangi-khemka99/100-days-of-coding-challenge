class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        # Iterate over the characters of the first string along with their indices
        for j, char in enumerate(strs[0]):
            # Check if all characters at the current index are the same across all strings
            if all(j < len(i) and i[j] == char for i in strs):
                common += char  # Append the character to the common prefix
            else:
                break  # Break the loop if characters are not the same
        return common
    #O(N * M)
    # N - len(strs) ; M - len(strs[0])