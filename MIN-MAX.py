POS_INF = 99
NEG_INF = -99
GRAPH_DEPTH = 4

ORDER = 0
MIN_MAX = 1
VALUE = 2
DEPTH = 3
PARENT = 4

MIN = 0
MAX = 1

# [Order, Min / Max, Value, Depth, Parent]
graph = [[0, 1, NEG_INF, 0, -1],
    [0, 0, POS_INF, 1, 0],
    [1, 0, POS_INF, 1, 0],
    [0, 1, NEG_INF, 2, 0],
    [1, 1, NEG_INF, 2, 0],
    [2, 1, NEG_INF, 2, 1],
    [3, 1, NEG_INF, 2, 1],
    [0, 0, POS_INF, 3, 0],
    [1, 0, POS_INF, 3, 0],
    [2, 0, POS_INF, 3, 1],
    [3, 0, POS_INF, 3, 1],
    [4, 0, POS_INF, 3, 2],
    [5, 0, POS_INF, 3, 2],
    [6, 0, POS_INF, 3, 3],
    [7, 0, POS_INF, 3, 3],
    [0, 1, 10, 4, 0],
    [1, 1, 11, 4, 0],
    [2, 1, 9, 4, 1],
    [3, 1, 12, 4, 1],
    [4, 1, 14, 4, 2],
    [5, 1, 15, 4, 2],
    [6, 1, 13, 4, 3],
    [7, 1, 14, 4, 3],
    [8, 1, 5, 4, 4],
    [9, 1, 2, 4, 4],
    [10, 1, 4, 4, 5],
    [11, 1, 1, 4, 5],
    [12, 1, 3, 4, 6],
    [13, 1, 22, 4, 6],
    [14, 1, 20, 4, 7],
    [15, 1, 21, 4, 7]]


def solve_min_max():
    for i in range(GRAPH_DEPTH, -1, -1):
        for child in graph:
            if child[DEPTH] == i:
                for parent in graph:
                    if parent[DEPTH] == child[DEPTH] - 1 and parent[ORDER] == child[PARENT]:
                        if parent[MIN_MAX] == MAX:
                            parent[VALUE] = get_max(parent[VALUE], child[VALUE])
                        elif parent[MIN_MAX] == MIN:
                            parent[VALUE] = get_min(parent[VALUE], child[VALUE])


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


solve_min_max()
ans_list = get_solution_list()
for x in graph:
    print(x)

print()
print("The Min Max List:")
print(ans_list)

print("\nThe Min Max Tree:")
tabs = 8
index = 0
for i in range(5):
    for _ in range(2**i):
        if i == 4:
            print(' ', end='')
        for _ in range(tabs):
            print('\t', end='')
        print(ans_list[index], end='')
        index = index + 1
        for _ in range(tabs):
            print('\t', end='')
        if i == 4:
            print('\t', end='')
    print('\n\n', end='')
    tabs = tabs // 2

