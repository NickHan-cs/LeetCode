class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n, cnt = len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    cnt += 1
                    nextList = [(i, j)]
                    while nextList:
                        r, c = nextList.pop()
                        for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                nextList.append((x, y))
                                grid[x][y] = '0'
        return cnt
