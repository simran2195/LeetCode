class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        degree = defaultdict(int)

        for road in roads:
            a, b = road
            degree[a] += 1
            degree[b] += 1

        max_rank = 0
        for i in range(0, n):
            for j in range(i+1, n):
                rank = degree[i] + degree[j]
                if [i,j] in roads or [j,i] in roads and i!=j:
                    rank -= 1
                
                max_rank = max(rank, max_rank)

        return max_rank

            

