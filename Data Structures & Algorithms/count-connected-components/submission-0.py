class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = dict()
        for i in range(n):
            adj_list[i] = []
        for edge in edges:
            start = edge[0]
            end = edge[1]
            adj_list[start].append(end)
            adj_list[end].append(start)
        # run dfs from every single point if not seen, 
        # and just count those
        seen = set()
        def dfs(node):
            seen.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        return count
        