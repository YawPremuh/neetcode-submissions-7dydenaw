class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        hasht = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hasht:
                return [hasht[diff], i]
            else:
                hasht[n] = i
        return []
            
            


        

            
        