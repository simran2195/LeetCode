# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# https://www.youtube.com/watch?v=KLlXCFG5TnA&ab_channel=NeetCode

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}
        
        for i, n in enumerate(nums) :
            diff = target-n
            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i

        return


