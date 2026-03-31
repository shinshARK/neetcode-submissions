class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqs = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key in count:
            freqs[count[key]].append(key)
        result = []
        print(freqs)
        for freq in reversed(freqs):
            if freq != []:
                for num in freq:
                    if k != 0:
                        result.append(num)
                        k -= 1

        print(result)
        return result
