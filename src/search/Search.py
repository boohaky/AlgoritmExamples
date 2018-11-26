def maxElement(list_to_search):
    if not isinstance(list_to_search, list):
        return -1
    len_list = len(list_to_search)
    if len_list == 1:
        return list_to_search[0]
    max_val = list_to_search[0]
    for pos in range(0, len_list):
        if list_to_search[pos] > max_val:
            max_val = list_to_search[pos]
    return 'Max element ' + str(max_val)


def binarySearch(list_to_search, element):
    low = 0
    high = len(list_to_search) - 1
    while low <= high:
        mid = (low + high) // 2
        if element < list_to_search[mid]:
            high = mid - 1
        elif element > list_to_search[mid]:
            low = mid + 1
        else:
            return "Binary Search index " + str(mid)
    else:
        return "Binary Search " + "no number"


def pickNextTop(graph, visited_tops):
    for i in range(len(graph[0])):
        if i not in visited_tops:
            return i
    return -1


class DFS:

    def search(self, graph, value):
        graph_length = len(graph)
        graph_value = 0
        visited_tops = []
        while graph_value != value and len(visited_tops) < graph_length:
            visited_tops.append(graph_value)
            graph_value = self.dfs(graph, graph_value, visited_tops)
            if graph_value == -1:
                graph_value = pickNextTop(graph, visited_tops)
        if graph_value != value:
            return str(value) + " not found"
        else:
            return str(value) + " found"

    def dfs(self, graph, top, visited_tops):
        for i in range(len(graph[top])):
            if graph[top][i] != 0 and i not in visited_tops:
                return i
        return -1


class BFS:

    def search(self, graph, value):
        graph_length = len(graph)
        graph_value = 0
        visited_tops = [graph_value]
        while graph_value != value and len(visited_tops) < graph_length:
            graph_value = self.bfs(graph, value, graph_value, visited_tops)
            if graph_value == -1:
                graph_value = pickNextTop(graph, visited_tops)
        if graph_value != value:
            return str(value) + " not found"
        else:
            return str(value) + " found"

    def bfs(self, graph, searched_value, top, visited_tops):
        for i in range(len(graph[top])):
            if graph[top][i] != 0:
                visited_tops.append(i)
                if i == searched_value:
                    return i
        return -1


if __name__ == '__main__':
    print(maxElement([45, 20, 5, 9, 6]))
    print(binarySearch([5, 6, 9, 45, 150, 180], 5))
    graph = [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 0],
             [0, 1, 0, 0]]
    print(DFS().search(graph, 3))
    print(BFS().search(graph, 3))
