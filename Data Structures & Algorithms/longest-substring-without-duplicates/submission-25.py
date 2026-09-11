class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seq = set()
        max_len = 0

        while r < len(s):
            ch = s[r]

            while ch in seq:
                seq.remove(s[l])
                l += 1

            seq.add(ch)
            max_len = max(r-l+1, max_len)
            r += 1

        return max_len


        