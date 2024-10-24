# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# https://www.youtube.com/watch?v=cQ1Oz4ckceM&ab_channel=NeetCode
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # numbers is non decreasing

        l, r = 0, len(numbers)-1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1

            elif curSum < target:
                l += 1
            
            else:
                return [l + 1, r + 1]
        return

