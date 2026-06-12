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
        parent = dict()
        depth_node = dict()
        stack = list()
        visited = set()
        stack.append((1, 0))
        parent[1] = -1

        while stack:
            node, depth = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            depth_node[node] = depth
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1))
                    parent[neighbor] = node

        for query in queries:
            node1, node2 = query
            lca = self.lca(node1, node2, parent, depth_node)
            distance = depth_node[node1] + depth_node[node2] - 2 * depth_node[lca]
            if distance == 0:
                result.append(0)
                continue

            result.append(pow(2, distance - 1, 10**9 + 7))
        return result

    def lca(self, node1, node2, parent, depth_node):
        while depth_node[node1] > depth_node[node2]:
            node1 = parent[node1]
        while depth_node[node2] > depth_node[node1]:
            node2 = parent[node2]
        while node1 != node2:
            node1 = parent[node1]
            node2 = parent[node2]
        return node1
