POS_INF = 99
NEG_INF = -99
GRAPH_DEPTH = 4

ORDER = 0
MIN_MAX = 1
VALUE = 2
ALPHA = 3
BETA = 4
DEPTH = 5
PARENT = 6
INDEX = 7

MIN = 0
MAX = 1

# {Order, Min/Max, Value, alpha, beta, Depth, Parent, Index}
graph = [[0, MAX, NEG_INF, NEG_INF, POS_INF, 0, -1, 0],
    [0, MIN, POS_INF, NEG_INF, POS_INF, 1, 0, 1],
    [1, MIN, POS_INF, NEG_INF, POS_INF, 1, 0, 2],
    [0, MAX, NEG_INF, NEG_INF, POS_INF, 2, 0, 3],
    [1, MAX, NEG_INF, NEG_INF, POS_INF, 2, 0, 4],
    [2, MAX, NEG_INF, NEG_INF, POS_INF, 2, 1, 5],
    [3, MAX, NEG_INF, NEG_INF, POS_INF, 2, 1, 6],
    [0, MIN, POS_INF, NEG_INF, POS_INF, 3, 0, 7],
    [1, MIN, POS_INF, NEG_INF, POS_INF, 3, 0, 8],
    [2, MIN, POS_INF, NEG_INF, POS_INF, 3, 1, 9],
    [3, MIN, POS_INF, NEG_INF, POS_INF, 3, 1, 10],
    [4, MIN, POS_INF, NEG_INF, POS_INF, 3, 2, 11],
    [5, MIN, POS_INF, NEG_INF, POS_INF, 3, 2, 12],
    [6, MIN, POS_INF, NEG_INF, POS_INF, 3, 3, 13],
    [7, MIN, POS_INF, NEG_INF, POS_INF, 3, 3, 14],
    [0, MAX, 10, NEG_INF, POS_INF, 4, 0, 15],
    [1, MAX, 11, NEG_INF, POS_INF, 4, 0, 16],
    [2, MAX, 9, NEG_INF, POS_INF, 4, 1, 17],
    [3, MAX, 12, NEG_INF, POS_INF, 4, 1, 18],
    [4, MAX, 14, NEG_INF, POS_INF, 4, 2, 19],
    [5, MAX, 15, NEG_INF, POS_INF, 4, 2, 20],
    [6, MAX, 13, NEG_INF, POS_INF, 4, 3, 21],
    [7, MAX, 14, NEG_INF, POS_INF, 4, 3, 22],
    [8, MAX, 5, NEG_INF, POS_INF, 4, 4, 23],
    [9, MAX, 2, NEG_INF, POS_INF, 4, 4, 24],
    [10, MAX, 4, NEG_INF, POS_INF, 4, 5, 25],
    [11, MAX, 1, NEG_INF, POS_INF, 4, 5, 26],
    [12, MAX, 3, NEG_INF, POS_INF, 4, 6, 27],
    [13, MAX, 22, NEG_INF, POS_INF, 4, 6, 28],
    [14, MAX, 20, NEG_INF, POS_INF, 4, 7, 29],
    [15, MAX, 21, NEG_INF, POS_INF, 4, 7, 30]]


def get_solution_list():
    ans = []
    for g in graph:
        ans.append(g[VALUE])
    return ans


def get_min(v1, v2):
        if v1 < v2:
            return v1
        return v2


def get_max(v1, v2):
        if v1 > v2:
            return v1
        return v2

test = []
test.append(graph[0])
test_graph = graph.copy()

depth = 1
parent_order = 0

for _ in range(1000):
    for g in test_graph:
        if g[ALPHA] < g[BETA]:
            if g[DEPTH] == depth and g[PARENT] == parent_order:
                test.append(g)
                depth += 1
                parent_order = g[ORDER]
    while True:
        if len(test) == 0:
            break
        temp_child = test.pop()
        if len(test) == 0:
            break
        temp_parent = test.pop()
        if temp_parent[MIN_MAX] == MIN:
            if temp_child[VALUE] < temp_parent[BETA]:
                graph[temp_parent[INDEX]][BETA] = graph[temp_child[INDEX]][VALUE]
                if graph[temp_parent[INDEX]][ALPHA] >= graph[temp_parent[INDEX]][BETA]:
                    graph[temp_parent[INDEX]][VALUE] = graph[temp_parent[INDEX]][BETA]
                    test_graph.remove(temp_child)
                    test.append(graph[temp_parent[INDEX]])
                else:
                    depth = temp_parent[DEPTH] + 1
                    parent_order = temp_parent[ORDER]
                    test_graph.remove(temp_child)
                    break
            else:
                depth = temp_parent[DEPTH] + 1
                parent_order = temp_parent[ORDER]
                test_graph.remove(temp_child)
                break

        else:
            if temp_child[VALUE] > temp_parent[ALPHA]:
                graph[temp_parent[INDEX]][ALPHA] = graph[temp_parent[INDEX]][VALUE]
                if graph[temp_parent[INDEX]][ALPHA] >= graph[temp_parent[INDEX]][BETA]:
                    graph[temp_parent[INDEX]][VALUE] = graph[temp_parent[INDEX]][ALPHA]
                    test_graph.remove(temp_child)
                    test.append(graph[temp_parent[INDEX]])
                else:
                    depth = temp_parent[DEPTH] + 1
                    parent_order = temp_parent[ORDER]
                    test_graph.remove(temp_child)
                    break
            else:
                depth = temp_parent[DEPTH] + 1
                parent_order = temp_parent[ORDER]
                test_graph.remove(temp_child)
                break


for g in graph:
    print(g)
