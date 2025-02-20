class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def bfs(r, c):
            # look in horizontal and vertical 1 step of r, c. if not visited, call bfs

            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    # check if is it 1, not in visited and index check
                    if (r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == "1"):
                        q.append((r,c))
                        visited.add((r,c))

                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    num_islands += 1

        return num_islands

            

