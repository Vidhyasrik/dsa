"""
LeetCode#207
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
def canFinish(numCourses, preRequisites):
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in preRequisites:
        preMap[crs].append(pre)
    # visitSet = all courses along the curr DFS path
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
    for crs in range(numCourses):
        if not dfs(crs): return False
    return True


numCourses = 2 
prerequisites = [[1, 0]]
print("canFinish:=>", canFinish(numCourses, prerequisites))
numCourses = 2
prerequisites = [[1,0],[0,1]]
print("canFinish:=>", canFinish(numCourses, prerequisites))

# Method#2
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Determines if it is possible to finish all courses given prerequisites.

        Args:
            numCourses: The number of courses.
            prerequisites: A list of prerequisite pairs, where prerequisites[i] = [ai, bi]
                           indicates that you must take course bi first if you want to take course ai.

        Returns:
            True if it is possible to finish all courses, False otherwise.
        """

        # Build the graph and in-degree counts
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre_req in prerequisites:
            graph[pre_req].append(course)
            in_degree[course] += 1

        # Initialize the queue with courses that have no prerequisites
        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        count = 0

        # Perform topological sort
        while queue:
            course = queue.pop(0)
            count += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If we have visited all courses, it means there is no cycle
        return count == numCourses
    
numCourses = 2 
prerequisites = [[1, 0]]
print("canFinish:=>", canFinish(numCourses, prerequisites))
numCourses = 2
prerequisites = [[1,0], [0,1]]
print("canFinish:=>", canFinish(numCourses, prerequisites))
