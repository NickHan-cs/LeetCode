class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(0, l - 1):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
