class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        res = []
        
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_seq = [curr_num]

                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_seq.append(curr_num)
                
                if len(curr_seq) > len(res):
                    res = curr_seq

        return len(res)
                

     