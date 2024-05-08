class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber:
            columnNumber -= 1
            title = chr(columnNumber % 26 + ord('A')) + title
            columnNumber //= 26
        return title