class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            chars = [0] * 26

            for char in string:
                charIndex = ord(char) - ord("a")
                chars[charIndex] += 1
            
            if tuple(chars) not in anagrams:
                anagrams[tuple(chars)] = [string]
            else:
                anagrams[tuple(chars)].append(string)

        return list(anagrams.values())
        