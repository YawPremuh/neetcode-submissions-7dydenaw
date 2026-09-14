class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '}':'{',
            ']':'[',
            ')':'(',
        }

        Stack = []

        for ch in s:
            if ch in brackets.values():
                Stack.append(ch)

            elif Stack and brackets[ch] == Stack[-1]:
                Stack.pop()

            else:
                return False

        return len(Stack) == 0