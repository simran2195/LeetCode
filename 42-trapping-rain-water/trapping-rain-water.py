# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# https://www.youtube.com/watch?app=desktop&v=ZI2z5pq0TqA&ab_channel=NeetCode

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]  # Track max heights
        water = 0  # Total water trapped

        while l < r:
            if height[l] < height[r]:
            # Water trapped depends on the left_max height
                if height[l] >= left_max:
                    left_max = height[l]  # Update left_max
                else: # If the current height is less than the max height seen so far, it can trap water.
                    water += left_max - height[l]  # Add trapped water
                l += 1  # Move the left pointer

            else:
                if height[r] >= right_max:
                    right_max = height[r]  # Update right_max
                else:
                    water += right_max - height[r]  # Add trapped water
                r -= 1  # Move the right pointer

        return water

