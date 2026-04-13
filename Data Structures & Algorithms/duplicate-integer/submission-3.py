class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        seen = set()
        result = []

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False