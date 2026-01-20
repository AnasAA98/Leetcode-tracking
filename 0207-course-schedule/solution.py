class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            prereq[course].append(preq)
        visited =  set()
        def explore(crs) -> bool:
            if crs in visited:
                return False
            if prereq[crs] == []:
                return True
            visited.add(crs)
            for preq in prereq[crs]:
                if not explore(preq):
                    return False
            visited.remove(crs)
            prereq[crs] = []
            return True
        for crs in range(numCourses):
            if not explore(crs):
                return False
        return True
