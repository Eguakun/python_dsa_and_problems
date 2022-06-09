# Time complexity: O(n + p) where n is number of nodes and p is number of pre requisites
def canFinish(numCourses, prerequisites):
    preMap = {i:[] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visitSet = set()
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True

        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): 
                return False
        visitSet.remove(crs)
        preMap[crs] = []
        return True

    # we must loop like this because what if our graph isnt connected?
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True
