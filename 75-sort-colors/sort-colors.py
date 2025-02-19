class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 - red
        # 1 - white
        # 2 - blue

        count = [0]*3
        for num in nums:
            count[num] += 1
        
        i = 0
        for j in range(3):
            while count[j]:
                count[j] -= 1
                nums[i] = j
                i += 1

    

            
        


            
        