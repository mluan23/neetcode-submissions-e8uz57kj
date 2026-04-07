class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # basically check for cycles.
    
        seen = set()
        # needing the parent since undirected
        def dfs(adj_list, node):
            # if can get ot every node, then connected
            seen.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    dfs(adj_list, neighbor)
        
        adj_list = dict()
        for i in range(n):
            adj_list[i] = []
        for edge in edges:
            start = edge[0]
            end = edge[1]
            adj_list[start].append(end)
            adj_list[end].append(start)
        # check is connected and acyclic
        dfs(adj_list, 0)
        if len(seen) != n:
            return False
        return n - 1 == len(edges)

