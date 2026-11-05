class Solution:

    def encode(self, strs: List[str]) -> str:
        key = "*"
        string = key
        for s in strs: 
            string += "/"
            string += "|".join(str(ord(c) + ord(key)) for c in s)
            
        return string;

    def decode(self, s: str) -> List[str]:
        res = []

        words = s.split("/")
        key = words[0]

        for i in range (1, len(words)):
            word = ""
            encoded = words[i].split("|")
            for val in encoded:
                if val:
                    word += "".join(chr(int(val) - ord(key)))
                else: 
                    word += ""
            res.append(word)
        
        return res




