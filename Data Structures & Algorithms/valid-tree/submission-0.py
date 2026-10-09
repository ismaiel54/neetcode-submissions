class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        def dfs(i, prev):
            if i in seen:
                return False
            seen.add(i)
            for nei in graph[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                   return False
            return True

        return dfs(0, -1) and len(seen) == n
        

            
