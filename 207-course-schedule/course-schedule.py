class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #  create an adjacency list
        preMap = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            preMap[course].append(pre)
            
        visitSet = set()
        
        def dfs(course):
            if course in visitSet:
                return False #loop detected
            
            # no prereq needed
            if preMap[course] == []:
                return True
            
            visitSet.add(course)
            # visit prereqs of this course
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
                    
            visitSet.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
                
        return True