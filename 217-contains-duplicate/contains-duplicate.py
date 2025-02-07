class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums_set = set()

        # for element in nums:
        #     if element not in nums_set:
        #         nums_set.add(element)
        #     else:
        #         return True

        # return False

        # more optimized solution
        # check if lengeth of nums and lengeth is set of nums is unequal

        return len(nums) > len(set(nums))


