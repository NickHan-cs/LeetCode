from typing import List


class Solution:
    def mergeCount(self, prefix_s: List[int], lower: int, upper: int, left: int, right: int) -> int:
        if len(prefix_s) == 1:
            return 0
        if left >= right:
            if lower <= prefix_s[left] <= upper:
                return 1
            return 0
        mid = (left + right) // 2
        cnt = 0
        cnt += self.mergeCount(prefix_s, lower, upper, left, mid)
        cnt += self.mergeCount(prefix_s, lower, upper, mid + 1, right)
        left_pos = left
        lo_pos = mid + 1
        up_pos = mid + 1
        while left_pos <= mid:
            while lo_pos <= right and prefix_s[lo_pos] - prefix_s[left_pos] < lower:
                lo_pos += 1
            while up_pos <= right and prefix_s[up_pos] - prefix_s[left_pos] <= upper:
                up_pos += 1
            cnt += up_pos - lo_pos
            left_pos += 1
        prefix_s1 = prefix_s[:]
        i = left
        j = mid + 1
        k = 0
        while i <= mid and j <= right:
            if prefix_s1[i] <= prefix_s1[j]:
                prefix_s[left + k] = prefix_s1[i]
                k += 1
                i += 1
            else:
                prefix_s[left + k] = prefix_s1[j]
                k += 1
                j += 1
        if i <= mid:
            prefix_s[left + k: right + 1] = prefix_s1[i: mid + 1]
        else:
            prefix_s[left + k: right + 1] = prefix_s1[j: right + 1]
        return cnt

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        length = len(nums)
        prefix_s = [0]
        for i in range(length):
            prefix_s.append(prefix_s[-1] + nums[i])
        return self.mergeCount(prefix_s, lower, upper, 1, length)
