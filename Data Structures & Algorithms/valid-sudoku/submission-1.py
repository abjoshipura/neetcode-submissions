class Solution:
    def isValid(self, lists: List[str]) -> bool:
        for element in lists:
            filtered_nums = [x for x in element if x != "."]
            if len(filtered_nums) != len(set(filtered_nums)):
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Rows
        rows = board

        # Check Columns
        cols = [[] for _ in range(9)]
        for i in range(9):
            for row in board:
                cols[i].append(row[i])
        
        # Check Boxes
        boxes = [[] for _ in range(9)]
        for i in range(3):
            subrows = board[i * 3: i * 3 + 3]
            
            boxes[i * 3] += subrows[0][0:3] + subrows[1][0:3] + subrows[2][0:3]
            boxes[i * 3 + 1] += subrows[0][3:6] + subrows[1][3:6] + subrows[2][3:6]
            boxes[i * 3 + 2] += subrows[0][6:9] + subrows[1][6:9] + subrows[2][6:9]
        
        return self.isValid(rows) and self.isValid(cols) and self.isValid(boxes)