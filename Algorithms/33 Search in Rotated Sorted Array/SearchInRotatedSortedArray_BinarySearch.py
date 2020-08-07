from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left, right = 0, l - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[l - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
sol = Solution()
print(sol.search(nums, target))
