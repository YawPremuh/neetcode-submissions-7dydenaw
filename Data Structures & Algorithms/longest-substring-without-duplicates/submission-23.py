class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        l = 0
        longest = 0

        for r in range(len(s)):
            ch = s[r]

            if ch in seen:
                l = max(l, seen[ch] + 1)

            seen[ch] = r
            longest = max(r-l+1, longest)

        return longest