class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        isomeric_dict = {}
        for i in range(len(s)):
            if s[i] not in isomeric_dict:
                if t[i] in isomeric_dict.values():
                    return False
                isomeric_dict[s[i]] = t[i]
            elif isomeric_dict[s[i]] != t[i]:
                return False
        
        return True
    #O(N)