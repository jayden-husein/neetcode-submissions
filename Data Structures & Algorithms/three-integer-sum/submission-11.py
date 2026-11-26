class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue 
            k, j = i + 1, len(nums) - 1
            while k < j:
                sum = a + nums[k] + nums[j]
                if sum < 0: 
                    k += 1
                elif sum > 0:
                    j -= 1
                else:
                    res.append([a, nums[k], nums[j]])
                    # want to keep checking all possible solutions (?)
                    k += 1
                    while nums[k] == nums[k-1] and k < j:
                        k += 1

        return res