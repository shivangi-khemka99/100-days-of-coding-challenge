class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pos1,pos2 = 0,0
        while pos1<len(pushed) and pos2<len(popped):
            stack.append(pushed[pos1])
            while(stack and stack[-1] == popped[pos2]):
                stack.pop()
                pos2+=1
            pos1+=1
        
        return not stack 