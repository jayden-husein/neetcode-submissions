class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for index, num in enumerate(nums): 
            complements[num] = index

        for index, num in enumerate(nums):
            if target - num in complements and index != complements[target - num]:
                return [index, complements[target - num]]