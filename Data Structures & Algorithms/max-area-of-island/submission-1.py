class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(node: tuple):
            def getNeighbors(cell: tuple) -> list:
                offsets = ((-1, 0), (0, -1), (1, 0), (0, 1))

                neighbors = list()
                for offset in offsets:
                    nX = cell[0] + offset[0]
                    nY = cell[1] + offset[1]

                    if 0 <= nX < h and 0 <= nY < w and grid[nX][nY]:
                        neighbors.append((nX, nY))
                
                return neighbors

            island = list()

            stack = list()
            visited = set()

            stack.append(node)
            while stack:
                node = stack.pop(-1)

                for neighbor in getNeighbors(node):
                    if neighbor not in visited:
                        stack.append(neighbor)

                visited.add(node)

            return visited

        h = len(grid)
        w = len(grid[0])

        islands = list()
        visited = set()

        maxArea = 0
        for i in range(h):
            for j in range(w):
                if not grid[i][j] or (i, j) in visited:
                    continue
                
                dfs_visited = dfs((i, j))
                maxArea = max(maxArea, len(dfs_visited))

                islands.append(list(dfs_visited))
                visited.update(dfs_visited)

        return maxArea