class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Define a cache
        cache = [{}]
        return self.dfs(m, n, startRow, startColumn, maxMove, cache)

    def dfs(self, m, n, i, j, remaining, cache):
        # Define possible moves
        moves = [(1,0), (-1, 0), (0,1), (0,-1)]
        if (i, j, remaining) in cache[0]:
            return cache[0][(i, j, remaining)]
        if i < 0 or i == m or j < 0 or j == n:
            return 1
        if remaining == 0:
            return 0
        ans = 0
        for (x, y) in moves:
            ans = (ans + self.dfs(m, n, i + x, j + y, remaining - 1, cache)) % (10 ** 9 + 7)
        cache[0][(i, j, remaining)] = ans
        return ans
