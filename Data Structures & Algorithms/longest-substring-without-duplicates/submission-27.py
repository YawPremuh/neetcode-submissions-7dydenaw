class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hash_map = {}
        max_len = 0

        while r < len(s):
            ch = s[r]

            if ch in hash_map:
                l = max(l, hash_map[ch] + 1)

            hash_map[ch] = r
            max_len = max(r-l+1, max_len)
            r += 1

        return max_len



        