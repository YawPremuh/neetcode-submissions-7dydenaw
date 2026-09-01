import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, num))
            else:
                heapq.heappushpop(heap, (cnt, num))

        return [c[1] for c in heap]