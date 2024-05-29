class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        int_value = int(s, 2)
        while int_value != 1:
            if int_value % 2 == 0:
                int_value //=2
            else:
                int_value+=1
            steps+=1
        return steps