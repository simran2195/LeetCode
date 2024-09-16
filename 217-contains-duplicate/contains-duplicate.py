class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_1 = len(nums)
        len_2 = len(set(nums))


        if len_1 == len_2:
            return False
        else:
            return True  
        