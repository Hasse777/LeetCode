class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        graph = dict()
        for i, j in edges:
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []

            graph[i].append(j)
            graph[j].append(i)

        result = list()
        depth_node = dict()
        stack = list()
        visited = set()
        stack.append((1, 0))
        n = len(edges) + 1
        jump = len(edges).bit_length()
        up = [[-1] * jump for _ in range(n + 1)]

        while stack:
            node, depth = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            depth_node[node] = depth
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1))
                    up[neighbor][0] = node

        for j in range(1, jump):
            for i in range(1, n + 1):
                if up[i][j - 1] != -1:
                    up[i][j] = up[up[i][j - 1]][j - 1]

        for a, b in queries:
            p = self.lca(a, b, depth_node, up, jump)
            distance = depth_node[a] + depth_node[b] - 2 * depth_node[p]

            if distance == 0:
                result.append(0)
            else:
                result.append(pow(2, distance - 1, 10**9 + 7))
        return result

    def lca(self, node1, node2, depth_node, up, jump):
        if depth_node[node1] < depth_node[node2]:
            node1, node2 = node2, node1
        dif = depth_node[node1] - depth_node[node2]

        i = 0
        while dif:
            if dif & 1:
                node1 = up[node1][i]
            i += 1
            dif >>= 1

        if node1 == node2:
            return node1

        for i in range(jump - 1, -1, -1):
            if up[node1][i] != up[node2][i]:
                node1 = up[node1][i]
                node2 = up[node2][i]
        return up[node1][0]
