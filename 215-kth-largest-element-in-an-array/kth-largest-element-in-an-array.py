class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # approach 1 using heap - 
        # heapq.heapify(nums)
        # red = len(nums) - k
        # while red > 0 :
        #     red -= 1
        #     heapq.heappop(nums)

        # return nums[0]

        # approach 2: sort then return n-k

        nums.sort()
        return nums[len(nums)-k]