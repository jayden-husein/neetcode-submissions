class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = defaultdict(int)
        for c in s:
            s_freq[c] += 1
        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1

        return s_freq == t_freq