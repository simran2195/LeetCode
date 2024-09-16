class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        # len_1 = len(nums)
        # len_2 = len(set(nums))


        # if len_1 == len_2:
        #     return False
        # else:
        #     return True  
        