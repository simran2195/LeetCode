# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        found = -1

        for i in range(len(haystack)):

            if haystack[i:i+len(needle)] == needle:
                found = i
                return found


        return found
            

        