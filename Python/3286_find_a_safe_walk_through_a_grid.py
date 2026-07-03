import heapq

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        if health <= 0:
            return False
        m, n = len(grid), len(grid[0])
        distance = [[float('inf')] * n for _ in range(m)]
        distance[0][0] = grid[0][0]
        heap = []
        heapq.heappush(heap, (distance[0][0], 0, 0))
        while heap:
            dist, x, y = heapq.heappop(heap)
            if dist > distance[x][y]:
                continue
            if x == m - 1 and y == n - 1 and health - dist >= 1:
                return True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_dist = dist + grid[nx][ny]
                    if new_dist < distance[nx][ny]:
                        distance[nx][ny] = new_dist
                        heapq.heappush(heap, (new_dist, nx, ny))
        return False
