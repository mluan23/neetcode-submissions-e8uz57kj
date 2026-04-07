class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj_list = {i: [] for i in range(numCourses)}
        in_deg = [0] * numCourses
        for course, prereq in prerequisites:
            in_deg[course] += 1
            adj_list[prereq].append(course)

        queue = deque([])

        for i in range(numCourses):
            if in_deg[i] == 0:
                queue.append(i)

        while queue:
            cur_prereq = queue.popleft()
            res.append(cur_prereq)

            for course in adj_list[cur_prereq]:
                in_deg[course] -= 1
                if in_deg[course] == 0:
                    queue.append(course)
        
        return res if max(in_deg) == 0 else []


        