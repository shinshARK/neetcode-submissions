class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for _str in strs:
            encoded += f"{len(_str)}#{_str}"
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j+1+length
        return result
