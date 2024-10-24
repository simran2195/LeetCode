class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all the triplets [nums[i], nums[j], nums[k]] 
        # such that i != j, i != k, and j != k, 
        # and nums[i] + nums[j] + nums[k] == 0.
        res = []
        nums.sort()        

        for i, a in enumerate(nums):
            # to avoid repeating 
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r : #if both numbers are same
                        l += 1

        return res


            