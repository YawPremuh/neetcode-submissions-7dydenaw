class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        longest = 0
        l = 0
        r = 0

        while r < len(s):
            ch = s[r]

            if ch in seen:
                l = max(l, seen[ch] + 1)

            seen[ch] = r
            longest = max(r-l+1, longest)
            r += 1

        return longest