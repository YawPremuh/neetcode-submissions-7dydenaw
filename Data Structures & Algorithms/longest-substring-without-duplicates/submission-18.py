class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seq = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in seq:
                seq.remove(s[l])
                l += 1

            seq.add(s[r])
            longest = max(len(seq), longest)

        return longest