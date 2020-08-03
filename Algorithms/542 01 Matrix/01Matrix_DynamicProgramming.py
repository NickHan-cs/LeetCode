from typing import List
import math


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        dist = [[math.inf] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        for i in range(m):
            for j in range(n):
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j < n - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
                if i < m - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
        return dist
