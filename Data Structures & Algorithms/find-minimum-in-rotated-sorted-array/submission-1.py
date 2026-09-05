class Solution:
    def findMin(self, nums: List[int]) -> int:
        x = nums[0];
        for i in range(len(nums)):
            if (nums[i]<x):
                x = nums[i];
            
        return x;


