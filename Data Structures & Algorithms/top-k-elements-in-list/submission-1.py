class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqs = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key in count:
            freqs[count[key]].append(key)
        result = []
        for freq in reversed(freqs):
            for num in freq:
                result.append(num)
                if len(result) == k:
                    return result
