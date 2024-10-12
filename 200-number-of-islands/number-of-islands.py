class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case of empty grid
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set() # can use 2D grid also, but sets are easier
        islands = 0

        def bfs(r, c): #bfs is iterative and not recursive 
            q = collections.deque()
            visited.add((r,c)) # add this position to the visited set
            q.append((r, c))

            while q:
                row, col = q.popleft() # pop this position and check its adjacent positions
                directions = [[1, 0 ], [-1,0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c ) not in visited: # the grid is made of strings
                    bfs(r,c) #run bfs on this cell
                    islands += 1 # only add if there's a 1 and we haven't visited the island

        return islands



