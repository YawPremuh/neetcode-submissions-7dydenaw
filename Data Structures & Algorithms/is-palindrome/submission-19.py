class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(ch.lower() for ch in s if ch.isalnum())

        l = 0
        r = len(word) - 1

        while l < r:
            if word[l] != word[r]:
                return False

            l += 1
            r -= 1

        return True