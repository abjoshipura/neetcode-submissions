class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Union-Find approach. Very Very Very expensive.
        islands = list()

        height = len(grid)
        width = len(grid[0])

        def getLandNeighbors(cell: tuple) -> list:
            offsets = ((-1, 0), (0, -1), (1, 0), (0, 1))

            neighbors = list()
            for offset in offsets:
                nX = cell[0] + offset[0]
                nY = cell[1] + offset[1]

                if 0 <= nX < height and 0 <= nY < width and grid[nX][nY]:
                    neighbors.append((nX, nY))
            
            return neighbors

        def find(cell: tuple) -> int:
            for i, island in enumerate(islands):
                if cell in island:
                    return i

            return -1
        
        for i in range(height):
            for j in range(width):
                if not grid[i][j]:
                    continue
                
                cell = (i, j)
                parentIslandIndex = find(cell)

                if parentIslandIndex != -1:
                    parentIsland = islands[parentIslandIndex]
                else:
                    parentIsland = set((cell, ))
                    islands.append(parentIsland)
                
                neighbors = getLandNeighbors(cell)
                for neighbor in neighbors:
                    connectedIslandIndex = find(neighbor)
                    if connectedIslandIndex != -1 and connectedIslandIndex != parentIslandIndex:
                        parentIsland.update(islands[connectedIslandIndex])
                        islands.pop(connectedIslandIndex)
                        parentIslandIndex = find(cell)
                    else:
                        parentIsland.add(neighbor)

        maxArea = 0
        for island in islands:
            maxArea = max(maxArea, len(island))

        return maxArea
        