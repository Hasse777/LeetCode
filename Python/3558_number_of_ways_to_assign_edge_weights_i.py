class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = dict()
        for i, j in edges:
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []

            graph[i].append(j)
            graph[j].append(i)

        max_depth = 0
        visited = set()
        stack = list()
        stack.append((1, 0))

        while stack:
            node, depth = stack.pop()
            if node in visited:
                continue

            visited.add(node)
            max_depth = max(max_depth, depth)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1))

        if max_depth == 0:
            return 0
        return pow(2, max_depth - 1, 10**9 + 7)
