class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_t = {}
        
        for i,num in enumerate(nums):
            diff = target - num

            if diff in hash_t.keys():
                return [hash_t[diff], i]
            else:
                hash_t[num] = i

         
        
        