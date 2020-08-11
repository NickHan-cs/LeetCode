class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        if right == -1:
            return False
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                right -= 1
        return nums[left] == target or nums[right] == target
