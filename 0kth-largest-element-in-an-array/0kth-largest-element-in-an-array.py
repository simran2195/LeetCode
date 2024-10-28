class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        red = len(nums) - k
        while red > 0 :
            red -= 1
            heapq.heappop(nums)

        return nums[0]