# 1492. The kth Factor of n 
# https://leetcode.com/problems/the-kth-factor-of-n/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        # Find factors of n
        # Sort factors of n
        # Return kth factor or -1 
        factors = []
        if n < 0: # check if n is positive
            return -1 
            
        if k < 0: # check if k is positive
            return -1  
            
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)
        
        print(factors)
        factors.sort()
        
        if len(factors) > k-1:
            return factors[k-1]
        else:
            return-1