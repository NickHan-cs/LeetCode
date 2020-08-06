from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1 or nums[l - 1] > nums[0]:
            return nums[0]
        mid, left, right = 0, 0, l - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1
        return nums[left]


inList = [2, 2, 0, 1, 2, 2]
sol = Solution()
print(sol.findMin(inList))
