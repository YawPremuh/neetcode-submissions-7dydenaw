class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[', '}':'{', ')':'('}
        Stack = []

        for ch in s:
            if ch in brackets.values():
                Stack.append(ch)
            else:
                if len(Stack) != 0 and brackets[ch] == Stack[-1]:
                    Stack.pop()
                else:
                    return False

        return True if len(Stack) == 0 else False