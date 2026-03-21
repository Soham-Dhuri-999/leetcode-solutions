"""Problem: Longest Substring Without Repeating Characters
LeetCode #3 — Medium
Given a string s, find the length of the longest 
substring without repeating characters.

Examples:
Input: s = "abcabcbb"  →  Output: 3  (substring "abc")
Input: s = "bbbbb"     →  Output: 1  (substring "b")"""


class Solution:
    
    def substring(self, s:str)-> str:
        
        left = 0
        seen= set()
        max_length =0
        
        for right in range(len(s)):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])
            
            max_length =max(max_length, right -left +1)
            
            
        return max_length
            
                
