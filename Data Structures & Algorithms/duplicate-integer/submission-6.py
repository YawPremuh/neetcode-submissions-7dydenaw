class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        hasht = set()

        for n in nums:
            if n in hasht:
                return True
            else:
                hasht.add(n)
        return False
