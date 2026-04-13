class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1   

        sortfreq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            result.append(sortfreq[i][0])

        return result



