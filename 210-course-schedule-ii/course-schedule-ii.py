class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # adjacency list of pre reqs
        preMap = {i: [] for i in range(numCourses)}
        for co, pre in prerequisites:
            preMap[co].append(pre)

        # Set to keep track of visited 
        visited, cycle = set(), set()
        # to store the order
        res = []

        # dfs
        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)

            for prereq in preMap[course]:
                if dfs(prereq) == False:  
                    return False


            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        # running dfs
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res
            