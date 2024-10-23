# 1151. Minimum Swaps to Group All 1's Together
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
# Soln: https://www.youtube.com/watch?v=FjEi39DHTkI&ab_channel=CodewithCarter

class Solution:
    def minSwaps(self, data: List[int]) -> int:

        len_data = len(data)
        n = data.count(1)
        # sliding window size = 3

        cur = min_swaps = data[:n].count(0)

        for i in range(n,len_data):
            cur += data[i-n]
            cur -= data[i]
            min_swaps = min (cur, min_swaps)

        
        return min_swaps


        

        
        