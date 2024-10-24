# 2422. Merge Operations to Turn Array Into a Palindrome
# https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        # 2 pointer approach 
        # Choose any two adjacent elements and replace them with their sum.

        l, r = 0, len(nums)-1
        ops = 0
        # rsum = lsum = None
        while l < r:
            if nums[l] == nums[r]:# If both elements are equal, move both pointers
                l += 1
                r -= 1
            
            elif nums[l] < nums[r]:  # Merge the smaller element on the left
                nums[l + 1] += nums[l]
                l += 1
                ops += 1

            else: # Merge the smaller element on the right
                nums[r-1] += nums[r]
                r -= 1
                ops += 1

        return ops

            
