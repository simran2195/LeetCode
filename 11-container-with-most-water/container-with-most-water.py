class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        max_water = 0

        while left < right:
            # Calculate the area formed by the lines at left and right pointers
            width = right - left
            current_water = min(height[left], height[right]) * width

            # Update the maximum water if the current area is larger
            max_water = max(max_water, current_water)


            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
            


        