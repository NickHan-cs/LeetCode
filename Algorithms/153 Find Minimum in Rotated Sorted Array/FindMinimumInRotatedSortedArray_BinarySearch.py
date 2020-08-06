from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1 or nums[l - 1] > nums[0]:
            return nums[0]
        left, right = 0, l-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

