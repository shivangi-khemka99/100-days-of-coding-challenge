from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_counts = Counter(text)
        return min(balloon_counts['b'], balloon_counts['a'], balloon_counts['l'] // 2, balloon_counts['o'] // 2, balloon_counts['n'])