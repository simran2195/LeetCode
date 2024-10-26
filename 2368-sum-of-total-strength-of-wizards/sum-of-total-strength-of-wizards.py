# class Solution:
#     def totalStrength(self, strength: List[int]) -> int:
        
#         # For a contiguous group of wizards 
#         # (i.e. the wizards' strengths form a subarray of strength
#         # total strength = The strength of the weakest wizard in the group.*
#         # The total of all the individual strengths of the wizards in the group.

#         # Return the sum of the total strengths of all contiguous groups of wizards. 
#         # Since the answer may be very large, return it modulo 109 + 7.

#         sum = 0
#         # look at all subgroups with i 
#         i = 0
#         L = i - 1
#         R = i + 1

#         for i in range(0, len(strength)):
#             # look for left subarrays
#             while L >= 0 and L < i:
#                 subarr = strength[L, i+1]

#             # look for left subarrays


MOD = 10**9 + 7

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)

        # Step 1: Compute prefix sums and prefix of prefix sums
        prefix = [0] * (n + 1)  # Prefix sum array
        for i in range(n):
            prefix[i + 1] = prefix[i] + strength[i]

        # Prefix of prefix sums
        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = prefix_prefix[i] + prefix[i]

        # Step 2: Find previous and next smaller elements using monotonic stack
        next_smaller = [n] * n  # Default is n (no next smaller element)
        prev_smaller = [-1] * n  # Default is -1 (no previous smaller element)

        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                index = stack.pop()
                next_smaller[index] = i
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                index = stack.pop()
                prev_smaller[index] = i
            stack.append(i)

        # Step 3: Calculate the total strength
        total_strength = 0
        for i in range(n):
            left = prev_smaller[i]
            right = next_smaller[i]

            # Sum of subarrays ending at 'i' and starting after 'left'
            left_sum = prefix_prefix[i + 1] - prefix_prefix[left + 1]

            # Sum of subarrays starting at 'i' and ending before 'right'
            right_sum = prefix_prefix[right + 1] - prefix_prefix[i + 1]

            # Contribution of strength[i] as the minimum
            contribution = strength[i] * (right_sum * (i - left) - left_sum * (right - i))
            total_strength = (total_strength + contribution) % MOD

        return total_strength
