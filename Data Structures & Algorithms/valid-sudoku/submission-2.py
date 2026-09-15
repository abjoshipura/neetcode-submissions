from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visitedRows = defaultdict(set)
        visitedCols = defaultdict(set)
        visitedBoxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue
                
                if value in visitedRows[i] or value in visitedCols[j] or value in visitedBoxes[(i // 3, j // 3)]:
                    return False

                visitedRows[i].add(board[i][j])
                visitedCols[j].add(board[i][j])
                visitedBoxes[(i // 3, j // 3)].add(board[i][j])
        
        print(visitedRows)
        print(visitedCols)
        print(visitedBoxes)

        return True
