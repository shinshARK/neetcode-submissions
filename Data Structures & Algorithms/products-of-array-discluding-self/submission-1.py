class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prefix[0] = nums[0]
        suffix = [1] * len(nums)
        suffix[len(nums) - 1] = nums[len(nums) -1]

        for i in range(len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        # print(prefix)
        # print(suffix)
        res = [0] * len(nums)
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = prefix[i-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= suffix[i+1]
        return res