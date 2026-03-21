""" Longest Repeating Character Replacement
LeetCode #424 — Medium

You are given a string s and an integer k.
You can replace at most k characters in the string 
with any character you want.

Find the length of the longest substring containing 
the same letter after at most k replacements.

Examples:
Input: s = "AABABBA", k = 1  →  Output: 4
Input: s = "ABAB", k = 2     →  Output: 4
Input: s = "AAAA", k = 0     →  Output: 4
"""

class Solution:
    def longest_repeating_substring(self, s: str, k: int)-> int:
        
        seen ={}
        left = 0
        max_count = 0
        max_length = 0
        for right in range(len(s)):
            window = right - left +1

            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1
                
            max_count = max(max_count,seen[s[right]])
            if (window - max_count) > k:
                
                seen[s[left]] -= 1
                left += 1
                
            max_length = max(max_length, right - left +1)
            
        return max_length