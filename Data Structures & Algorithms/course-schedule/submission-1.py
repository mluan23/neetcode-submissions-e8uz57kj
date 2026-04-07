class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topo sort
        adj_list = {i : [] for i in range(numCourses)}
        in_deg = [0] * numCourses
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_deg[course] += 1
        
        # find everything with indegree 0
        queue = deque([])
        for i in range(numCourses):
            if in_deg[i] == 0:
                queue.append(i)
        
        while queue:
            prereq = queue.popleft()
            for course in adj_list[prereq]:
                in_deg[course] -= 1
                if in_deg[course] == 0:
                    queue.append(course)
        return max(in_deg) == 0
            
            