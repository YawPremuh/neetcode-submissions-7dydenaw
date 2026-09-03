class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. initialize an empty result list
        2. initialize an empty hash map to store freq count
        3. store the freq of each num in a tocken bucket
        4. the tocken bucket is going to be in ascending order so, to get out desired output you should loop from the end to the start of the bucket 
        5 append if the idx is not empty
        6. return the result if the length of the result array is equal to k 
        """
        res = []
        freq = {}
        count = [[] for i in range(len(nums)+1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for num,cnt in freq.items():
            count[cnt].append(num)

        for i in range(len(count)-1, -1, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res




        

        