class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        if n < 2 or not roads:
            return 0
        graph = {i: [] for i in range(1, n+1)}
        for road in roads:
            graph[road[0]].append([road[1], road[2]])
            graph[road[1]].append([road[0], road[2]])

        queue = list()
        queue.append(1)
        visited = set()
        result = float('inf')
        while queue:
            city = queue.pop(0)
            if city in visited:
                continue
            visited.add(city)
            for neighbor, distance in graph[city]:
                result = min(result, distance)
                queue.append(neighbor)

        return result
