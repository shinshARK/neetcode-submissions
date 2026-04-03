class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        postfix = [0] * length
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        for i in range(1, length):
            prefix[i] = prefix[i-1] * nums[i]
        # print(prefix)
        for i in range(length - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        # print(postfix)
        res = [1] * length
        left, right = 1, 1
        for i in range(length):
            res[i] *= left
            res[length-i-1] *= right
            left = prefix[i]
            right = postfix[length-i-1]
        return res
        