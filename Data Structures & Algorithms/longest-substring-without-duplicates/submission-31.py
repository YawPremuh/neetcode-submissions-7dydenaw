class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = {}
        longest = 0
        l = 0

        for r, ch in enumerate(s):
            if ch in seq:
                l = max(l, seq[ch] + 1)

            seq[ch] = r
            longest = max(r-l+1, longest)

        return longest