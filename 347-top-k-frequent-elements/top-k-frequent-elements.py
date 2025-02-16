class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sub problems:
        # 1) Get frequencies of elements
        # 2) Get elements with top k frequencies
        
        # method 1 - hashmap of frequencies
        freq_map = defaultdict(int)

        for ele in nums:
            freq_map[ele] += 1

        res = sorted(freq_map, key=freq_map.get, reverse=True)[:k]
        return res

        

        # method 2 - collections.counter

        # heap of frequencies
        

