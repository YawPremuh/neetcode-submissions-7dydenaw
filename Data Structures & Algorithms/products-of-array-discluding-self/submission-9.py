class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ''' At each index we make 2 passes and multiply the items before 
        the curr index into and array called pre and the items after the 
        curr index called post. Then mul
            1. initialize an array of 0s for the res, post and pre
            2. the first index of the pre array should be equal to 1
            3. the last item of post index should be 1
            4. loop through pre from 1 to len(nums) and multiply
            5. loop through post from the last but 1 index and multiply\
            6. return res

        '''
        n = len(nums)
        res = [0] * n
        pre = [0] * n
        post = [0] * n

        pre[0] = 1
        post[n-1] = 1

        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        for i in range(n):
            res[i] = pre[i] * post[i]

        return res
