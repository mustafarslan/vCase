

# Kahn’s algorithm for Topological Sorting
# https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

class SecondQuestion:
    def __init__(self):
        self.V = 0

    def init(self, n):
        self.V = n

    def topological_sort(self, graph):

        in_degree = [0] * self.V

        for i in graph:
            for j in graph[i]:
                in_degree[j] += 1

        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        cnt = 0
        top_order = []

        while queue:
            u = queue.pop(0)
            top_order.append(u)

            for i in graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
            cnt += 1

        if cnt != self.V:
            print("There exists a cycle in the graph")

        return top_order

    def run(self, graph):
        return self.topological_sort(graph)

