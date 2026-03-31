class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += f"{len(string)}#{string}"
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                # print(f"s[j-1] is {s[j-1]} isdigit: {s[j-1].isdigit()}")
                j+=1
            
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
