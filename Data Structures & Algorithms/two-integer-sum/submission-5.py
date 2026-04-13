class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hasht:
                return [hasht[diff], i]
            else:
                hasht[num] = i
        return []


        
            


        

            
        