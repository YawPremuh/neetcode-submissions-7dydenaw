class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasht = {}

        for n in nums:
            if n in hasht:
                return True
            else:
                hasht[n] = n
        return False
