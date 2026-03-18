# Question: Given an array of integers and a target, return indices of two numbers that
# add up to target.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, n in enumerate(nums):
            needed = target - n

            if needed in seen:
                return [seen[needed], i]

            seen[n] = i
