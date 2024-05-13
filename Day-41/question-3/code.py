class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])

        #Flip the rows first
        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    grid[r][c] = 0 if grid[r][c] else 1
        
        #Flip the cols now
        for c in range(cols):
            one_count = 0
            for r in range(rows):
                one_count+= grid[r][c]
            if one_count < rows - one_count:
                for r in range(rows):
                    grid[r][c] = 0 if grid[r][c] else 1
        
        #Add bin numbers
        res = 0
        for r in range(rows):
            for c in range(cols):
                res+= grid[r][c] << (cols-c-1)
    
        return res