class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
            1. get the length of the each item in the strs list
            2. place the length and a # infront of the combined text
        '''
        res = []

        for s in strs:
            word = ''.join(s)
            count = len(word)

            res.append(str(count) + '#' + word)

        return ''.join(res)

            
    def decode(self, s: str) -> List[str]:
        '''
           1. initialize an empty result list
           2. use two pointers, ptr1 to identify when a new word begins
           3. ptr2 to identify the characters of the word
           4. move ptr2 int(s[ptr+1]) times while storing the characters in a new string and then append the new string to the result list 
        '''
        res = []
        ptr1 = 0

        while ptr1 < len(s):
            ptr2 = ptr1
            while s[ptr2] != '#':
                ptr2 += 1
            
            word_count = int(s[ptr1:ptr2])
            ptr1 = ptr2+1
            word = s[ptr1 : ptr1 + word_count]
            res.append(word)
            ptr1 += word_count

        return res
        
