class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_seq = 0
        for num in nums:
            if num - 1 not in numset:
                current = num
                seq_length = 0
                while current in numset:
                    current += 1
                    seq_length += 1
                if seq_length > longest_seq:
                    longest_seq = seq_length
        return longest_seq