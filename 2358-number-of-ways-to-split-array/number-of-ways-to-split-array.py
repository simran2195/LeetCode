class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        valid_splits = 0
        
        # Iterate through the array, excluding the last index
        for i in range(len(nums) - 1):
            left_sum += nums[i]  # Add current element to the left sum
            right_sum = total_sum - left_sum  # Calculate right sum dynamically
            
            # Check the condition for a valid split
            if left_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits