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
                sub = ''+char
                res += 1
            else:
                sub += char

        return res+1
    

