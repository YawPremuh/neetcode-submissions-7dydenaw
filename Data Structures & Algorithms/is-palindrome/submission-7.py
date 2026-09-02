class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_stack = []

        for ch in s:
            if ch.isalnum():
                s_stack.append(ch.lower())

        l = 0
        r = len(s_stack) - 1

        while l < r:
            if s_stack[l] == s_stack[r]:
                l += 1
                r -= 1
            else:
                return False

        return True