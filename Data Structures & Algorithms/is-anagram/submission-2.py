class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        map = {}
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1

        for char in t:
            if char in map:
                map[char] -= 1
            else:
                return False

        return all(v == 0 for v in map.values())