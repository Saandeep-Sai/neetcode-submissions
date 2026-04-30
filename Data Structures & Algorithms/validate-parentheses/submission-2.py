class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(","}":"{","]":"["}
        if len(s)%2 != 0: # Check if the len is even or odd if odd the string doesnt contain the required parentesis
            return False
        else:
            stack = []
            for i in s:
                if i in dic and stack and stack[-1] == dic[i]:
                    stack.pop()
                    continue
                stack.append(i)
        if len(stack) == 0:
            return True     
        else:
            return False