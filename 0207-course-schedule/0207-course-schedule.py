class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premp = { c:[] for c in range(numCourses)}
        for crs,pre in prerequisites:
            premp[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if premp[crs] == []:
                return True
            visit.add(crs)
            for pre in premp[crs]:
                if not dfs(pre):
                    return False
            premp[crs] = []
            visit.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True