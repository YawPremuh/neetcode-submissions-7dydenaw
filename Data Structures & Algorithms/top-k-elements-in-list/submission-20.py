import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for num,cnt in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, num))
            else:
                heapq.heappushpop(heap, (cnt, num))

        return [c[1] for c in heap]