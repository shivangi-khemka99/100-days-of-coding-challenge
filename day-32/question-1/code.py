class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                decoded_string = ""
                while stack[-1] != "[":
                    decoded_string = stack.pop() + decoded_string
                stack.pop()  # Pop the '['
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * decoded_string)
            else:
                stack.append(char)
        return "".join(stack)