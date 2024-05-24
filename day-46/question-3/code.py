from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_cnt = Counter(letters)
        def can_form_word(w):
            word_cnt = Counter(w)
            for c in word_cnt:
                if word_cnt[c] > letter_cnt[c]:
                    return False
            return True

        def word_score(w):
            return sum(score[ord(c) - ord('a')] for c in w)

        def helper(i, current_score):
            nonlocal max_score
            if i >= len(words):
                max_score = max(max_score, current_score)
                return

            # Option 1: Include words[i] if possible
            if can_form_word(words[i]):
                for c in words[i]:
                    letter_cnt[c] -= 1
                helper(i + 1, current_score + word_score(words[i]))
                for c in words[i]:
                    letter_cnt[c] += 1
            
            # Option 2: Do not include words[i]
            helper(i + 1, current_score)

        max_score = 0
        helper(0, 0)
        return max_score