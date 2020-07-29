from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, current):
            if len(current) == i + 1:
                allSubsets.append(current[:])
                # "current[:]" cannot be replaced by "current" because "allSubsets" appends A OBJECT not the values.
                # if "current" is used here and the value of "current" changes,
                # the value of "allSubsets" will also change.
            else:
                for j in range(first, len(nums)):
                    current.append(nums[j])
                    backtrack(j + 1, current)
                    current.pop()

        allSubsets = [[]]
        for i in range(len(nums)):
            backtrack(0, [])
        return allSubsets
