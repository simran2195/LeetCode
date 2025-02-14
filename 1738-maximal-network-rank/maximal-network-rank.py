class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        degree = defaultdict(int)
        road_set = set() # for efficiency 

        for road in roads:
            a, b = road
            degree[a] += 1
            degree[b] += 1
            road_set.add((a,b))
            road_set.add((b,a))

        max_rank = 0
        for i in range(0, n):
            for j in range(i+1, n):
                rank = degree[i] + degree[j]
                if (i, j) in road_set or (j, i) in road_set:
                    rank -= 1
                
                max_rank = max(rank, max_rank)

        return max_rank

            

