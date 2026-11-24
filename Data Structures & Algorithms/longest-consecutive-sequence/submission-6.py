class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = []

        for n in numbers:
            if n - 1 in numbers:
                continue 
            res.append([n])
            j = n
            while j + 1 in numbers:
                res[-1].append(j + 1)
                j += 1


        best = 0
        for n in res:
            if len(n) >= best: 
                best = len(n)

        return best
