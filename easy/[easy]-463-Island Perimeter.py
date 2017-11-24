class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # a (m*n) grid have (2mn+m+n) edges
        # 暂时没想到别的方法，只好遍历了
        
        row = len(grid)
        col = len(grid[0])
        p = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 : 
                    p += 4
                    if i>0 and grid[i-1][j] : 
                        p += -2
                    if j>0 and grid[i][j-1]:
                        p += -2
        return p
