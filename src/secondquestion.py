from collections import defaultdict


class SecondQuestion:
    def __init__(self):
        pass

    def init(self, n):
        self.V = n

    # The function to do Topological Sort.
    def topologicalSort(self, graph):

        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        in_degree = [0] * (self.V)

        # Traverse adjacency lists to fill indegrees of
        # vertices.  This step takes O(V + E) time
        for i in graph:
            for j in graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:

            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            top_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1

        # Check if there was a cycle
        if cnt != self.V:
            print("There exists a cycle in the graph")
        else:
            # Print topological order
            print(top_order)

    def run(self, graph):
        self.topologicalSort(graph)

