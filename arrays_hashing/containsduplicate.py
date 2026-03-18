# Question: Given an integer array, return true if any value appears at least twice.
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
