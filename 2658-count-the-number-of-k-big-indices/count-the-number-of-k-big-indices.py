# 2519. Count the Number of K-Big Indices
# https://leetcode.com/problems/count-the-number-of-k-big-indices/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
# Soln: https://www.youtube.com/watch?app=desktop&v=-zMGgsGq_Kg&ab_channel=CodewithCarter

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:

        count = 0

        # array of numbers that meet condition 1
        cond1_valid = [False] * len(nums)
        max_heap = []

        # Check if condition 1 is met

        for i, n in enumerate(nums):
            # if we have at least k numbers in heap, bec we want at least k numbers < number at index i on left of index i
            if len(max_heap) == k and -max_heap[0] < n:
                cond1_valid[i] = True 
            heappush(max_heap, -n)

            if len(max_heap) > k:
                heappop(max_heap)

        # check condition 2
        max_heap = []
        for i, n in reversed(list(enumerate(nums))):
            if len(max_heap) == k and -max_heap[0] < n and cond1_valid[i] == True:
                count += 1
            heappush(max_heap, -n)

            if len(max_heap) > k:
                heappop(max_heap)

        return count