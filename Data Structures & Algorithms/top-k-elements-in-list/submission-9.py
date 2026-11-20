class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for i in range(len(nums) + 1)]
        count_set = defaultdict(int)
        for num in nums: 
            count_set[num] += 1

        for key, val in count_set.items():
            counts[val].append(key)

        res = []
        for _ in range(k):
            i = len(counts) - 1
            while not counts[i]:
                i -= 1
            res.append(counts[i][0])
            del counts[i][0]

        return res