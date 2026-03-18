# Question: Given two strings s and t, return true if t is an anagram of s.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        book = {}

        for c in s:
            if c in book:
                book[c] += 1
            else:
                book[c] = 1

        for c in t:
            if c not in book:
                return False

            book[c] -= 1

            if book[c] < 0:
                return False

        return True
