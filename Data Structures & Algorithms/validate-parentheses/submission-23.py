class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []

        for ch in s:
            if ch in brackets.values():
                stack.append(ch)

            elif stack and brackets[ch] == stack[-1]:
                stack.pop()

            else:
                return False

        return False if stack else True