class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        seen = set()
        def dfs(crs):
            if crs in seen:
                return False
            if premap[crs] == []:
                return True
            seen.add(crs)
            
            for p in premap[crs]:
                if not dfs(p):
                    return False
            premap[crs] = []
            seen.remove(crs)
            return True


        for crs in premap:
            if not dfs(crs):
                return False
        return True
                
            
                

