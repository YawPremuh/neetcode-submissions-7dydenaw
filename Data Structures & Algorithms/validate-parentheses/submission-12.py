class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {'(': ')', '{' : '}', '[' : ']'}
        stack = []

        for bracket in s:
            if bracket in open_brackets.keys():
                stack.append(bracket)
            elif stack and bracket == open_brackets[stack[-1]]:
                stack.pop()
            else:
                return False
            
        if stack:
            return False
        else:
            return True