class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + '~' + word

        return res
        
    def decode(self, s: str) -> List[str]:
        l = 0
        r = 1
        decode_res = []
        str_found = ""

        while r < len(s):
            if s[r] == '~':
                count = int(s[l:r])

                while count > 0:
                    r += 1
                    str_found += s[r] 
                    count -= 1
    
                decode_res.append(str_found)
                str_found = ""
                l = r + 1
                r += 1 

            else:
                r += 1    

        return decode_res


            
            



        