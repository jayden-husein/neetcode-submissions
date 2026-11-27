class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, n in enumerate(nums):
            comp[n] = i
        
        for index, val in enumerate(nums):
            if target - val in comp and index != comp[target - val]:
                return [index, comp[target - val]]