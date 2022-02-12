from collections import defaultdict


class Utility:
    def __init__(self):
        pass

    # [[1,0], [2, 0], [3,1,2]]
    def convert_to_graph(self, input_list):
        graph = defaultdict(list)

        for item in range(input_list[0][0]):
            graph[item] = []

        for list_item in input_list:
            if len(list_item) > 2:
                for item in range(1, len(list_item)):
                    graph[list_item[item]].append(list_item[0])
            elif len(list_item) == 1:
                pass
            else:
                graph[list_item[1]].append(list_item[0])

        return graph