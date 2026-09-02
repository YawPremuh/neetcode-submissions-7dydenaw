class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        lon_seq = []

        for num in nums:

            if num - 1 not in numSet:
                curr_num = num
                curr_seq = [num]
            
                while curr_num + 1 in numSet:
                    curr_num += 1
                    curr_seq.append(curr_num)
                
                if len(curr_seq) > len(lon_seq):
                    lon_seq = curr_seq

        return len(lon_seq)