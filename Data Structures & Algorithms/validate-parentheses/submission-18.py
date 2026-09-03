class Solution:
    def isValid(self, s: str) -> bool:
        brack_pairs = {')':'(', ']':'[', '}':'{'}
        Stack = []

        for ch in s:
            if ch in brack_pairs:
                if len(Stack) != 0 and brack_pairs[ch] == Stack[-1]:
                    Stack.pop()
                else:
                    return False
            else:
                Stack.append(ch)
        
        return True if not Stack else False




