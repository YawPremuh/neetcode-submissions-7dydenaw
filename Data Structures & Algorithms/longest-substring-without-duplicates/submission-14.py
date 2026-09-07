class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        seen = {}

        while r < len(s):
            ch = s[r]

            if ch in seen:
                l = max(l, seen[ch]+1)

            seen[ch] = r
            longest = max(longest, r-l+1)
            r += 1

        return longest