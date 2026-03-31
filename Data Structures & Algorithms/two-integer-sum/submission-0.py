class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_hash = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in diff_hash:
                return [diff_hash[nums[i]], i]
            diff_hash[difference] = i
