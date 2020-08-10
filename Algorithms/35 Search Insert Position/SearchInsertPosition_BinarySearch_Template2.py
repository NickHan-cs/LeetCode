class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        ans, left, right = l, 0, l - 1
        while left <= right:
            mid = int((right - left) / 2) + left
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
