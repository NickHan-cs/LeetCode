class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if l == 0:
            return -1
        left, right = 0, l - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[0] < nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[l - 1]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
