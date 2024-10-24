# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# https://www.youtube.com/watch?v=KLlXCFG5TnA&ab_channel=NeetCode

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}
    
        for i, n in enumerate(nums) :
            diff = target-n
            # print("i = ", i, "n = ", n)
            # print("diff = ", diff)
            # print(prevMap) 
            if diff in prevMap:
                # print(prevMap[diff], i)
                return [prevMap[diff], i]

            prevMap[n] = i
            # print(f"Added prevMap[{n}] = {i}", "\n" )

        return


