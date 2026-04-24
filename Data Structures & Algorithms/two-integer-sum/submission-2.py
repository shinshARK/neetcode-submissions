class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffmap:
                return [diffmap[diff], i]
            diffmap[nums[i]] = i