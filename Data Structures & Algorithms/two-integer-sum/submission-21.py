class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_n = {}

        for i,num in enumerate(nums):
            diff = target - num

            if diff in hash_n:
                return [hash_n[diff], i]
            else:
                hash_n[num] = i