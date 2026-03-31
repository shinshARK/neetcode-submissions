class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            frequencies = [0] * 26
            for char in string:
                frequencies[ord(char) - ord('a')] += 1
            result[tuple(frequencies)].append(string)
        return list(result.values())
        