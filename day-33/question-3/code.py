class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        possible_values = []
        for i in range(len(number)):
            if number[i] == digit:
                possible_values.append(number[:i]+number[i+1:])
        return max(possible_values) if possible_values else number