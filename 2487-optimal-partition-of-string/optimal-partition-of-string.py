# 2405. Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency


class Solution:
    def partitionString(self, s: str) -> int:
        # the number of repeated letters is the subset
        # collections.counter
        # pick max frquency count

        res = 0
        sub = ''

        for char in s:
            if char in sub:
                # If the character is already in the current substring,
                # we finalize this partition and start a new one.
                sub = ''+char # Start a new substring with the current character
                res += 1 # Increment the partition counter
            else:
                # If the character is not in the current substring,
                # add it to the substring.
                sub += char

        return res+1
    

