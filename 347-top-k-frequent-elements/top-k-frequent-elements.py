class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sub problems:
        # 1) Get frequencies of elements
        # 2) Get elements with top k frequencies
        
        # method 1 - hashmap of frequencies
        # freq_map = defaultdict(int)

        # for ele in nums:
        #     freq_map[ele] += 1

        # res = sorted(freq_map, key=freq_map.get, reverse=True)[:k]
        # return res

        

        # method 2 - collections.counter
        # heap of frequencies

        # freq_map = Counter(nums)
        # heap = []
        # for num, freq in freq_map.items():
        #     heapq.heappush(heap, (-1*freq, num))
        #     # if len > k, pop last element
            

        # res = []
        # for i in range(0,k):
        #     res.append(heapq.heappop(heap)[1])

        # return res

        # method 3
        # Bucket sort
        freq_map = defaultdict(int)
        for ele in nums:
            freq_map[ele] += 1        
        
        n = len(nums)
        freq_count = [[] for i in range(0,n+1)]

        for num, freq in freq_map.items():
            freq_count[freq].append(num)

        res = []
        for i in range(n, 0, -1):
            for num in freq_count[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res








        

