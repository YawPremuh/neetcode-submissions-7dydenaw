class Solution:
    def isValid(self, s: str) -> bool:
        brack_pairs = {')':'(', ']':'[', '}':'{'}
        Stack = []

        if s[0] in brack_pairs.keys():
            return False

        for ch in s:
            if ch in brack_pairs.values():
                Stack.append(ch)
            else:
                if len(Stack) != 0 and brack_pairs[ch] == Stack[-1]:
                    Stack.pop()
                else:
                    Stack.append(ch)
        
        if len(Stack) == 0:
            return True
        else:
            return False




