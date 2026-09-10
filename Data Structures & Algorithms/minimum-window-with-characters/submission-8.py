class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        window = {}

        for ch in t:
            need[ch] = 1 + need.get(ch, 0)

        need_count = len(need)
        have = 0
        min_len = float("inf")
        res = ""
        l = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r + 1]

                left_ch = s[l]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                l += 1

        return res
