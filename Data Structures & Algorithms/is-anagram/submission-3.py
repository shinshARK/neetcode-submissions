class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        for _char in s:
            s_hash[_char] += 1
        for _char in t:
            t_hash[_char] += 1
        for key in s_hash:
            if s_hash[key] != t_hash.get(key, 0):
                return False
        return True


        