class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            word = ''.join(s)
            word_len = len(word)
            res.append(str(word_len)+'#'+word)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        ptr1 = 0

        while ptr1 < len(s):
            ptr2 = ptr1

            while s[ptr2] != '#':
                ptr2 += 1

            word_len = int(s[ptr1:ptr2])
            ptr1 = ptr2 + 1
            res.append(s[ptr1:ptr1 + word_len])
            ptr1 += word_len

        return res 
            
                
