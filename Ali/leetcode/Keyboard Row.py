class Solution:
    def findWords(self, words):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        result = []
        for word in words:
            x1 = all(char in row1 for char in word.lower())
            x2 = all(char in row2 for char in word.lower())
            x3 = all(char in row3 for char in word.lower())
            if x1 or x2 or x3:
                result.append(word)
        return result

