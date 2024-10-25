class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        res = float('inf')
        nums.sort()

        for i in range(len(nums)-2):

            # if there's a duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i+1, len(nums)-1

            while l < r:

                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < abs(res - target):
                    res = current_sum

                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1

        return res
