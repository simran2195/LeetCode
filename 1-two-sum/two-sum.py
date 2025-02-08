# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# https://www.youtube.com/watch?v=KLlXCFG5TnA&ab_channel=NeetCode

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # Method 1
        # O(n^2) time complexity
        # Brute Force method

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i, j]

        # Method 2
        # 1 pass using a hashmap
        # Time complexity: O(n)
        # Space complexity: O(n)

        prev_values = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in prev_values:
                return [prev_values[diff], i]

            prev_values[val] = i

        
        
     


