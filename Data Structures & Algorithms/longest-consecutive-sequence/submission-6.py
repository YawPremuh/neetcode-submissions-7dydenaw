class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        longest = 0

        for num in nums:

            if num - 1 not in numSet:
                curr_num = num
                curr_len = 1
            
                while curr_num + 1 in numSet:
                    curr_num += 1
                    curr_len += 1
                
                if curr_len > longest:
                    longest = curr_len

        return longest