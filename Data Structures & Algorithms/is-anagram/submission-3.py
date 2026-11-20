class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = defaultdict(int)
        for char in s:
            set_s[char] += 1

        set_t = defaultdict(int)
        for char in t:
            set_t[char] += 1

        if set_s == set_t:
            return True
        return False