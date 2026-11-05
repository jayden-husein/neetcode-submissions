class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs: 
            string += "/"
            string += "|".join(str(ord(c)) for c in s)
            
            
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        res = []

        words = s.split("/")

        for i in range (1, len(words)):
            word = ""
            encoded = words[i].split("|")
            for val in encoded:
                if val:
                    word += chr(int(val))
                else: 
                    word += ""
            res.append(word)
        
        return res




