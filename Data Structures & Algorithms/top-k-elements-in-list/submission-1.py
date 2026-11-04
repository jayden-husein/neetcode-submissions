class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []
        for n in nums:
            freq[n] = freq[n] + 1
        
        for i in range(k):
            max = [None, None]
            for index, (key, value) in enumerate(freq.items()):
                if max[1] is None or max[1] < value:
                    max = [key, value]
                
            res.append(max[0])
            freq.pop(max[0])

        return res