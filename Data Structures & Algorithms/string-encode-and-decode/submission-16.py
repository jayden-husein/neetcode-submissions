class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs: 
            res.append(str(len(s)))
            res.append('#')
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        j = 0
        res = []
        while j < len(s):
            i = j
            while s[j] != '#':
                j += 1
            counter = int(s[i:j])

            i = j + 1
            j += counter + 1
            res.append(s[i:j])
        
        return res
