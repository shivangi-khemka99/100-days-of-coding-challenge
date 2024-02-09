class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dic = dict()
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] in pattern_dic:
                if pattern_dic[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in pattern_dic.values():
                    return False
                pattern_dic[pattern[i]] = s[i]
        return True