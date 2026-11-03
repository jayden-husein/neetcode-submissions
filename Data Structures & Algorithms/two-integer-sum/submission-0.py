class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [map.get(complement), i]

            if nums[i] not in map:
                map[nums[i]] = i
            
        
