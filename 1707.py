from collections import deque
import sys

input = sys.stdin.readline

k = int(input())

# graph = [ [], [2], [1], [4], [3] ]
# graph = [ [], [3], [], [1, 4], [3] ]

def bfs(start):
    dq = deque()
    dq.append(start)
    color[start] = 0

    while dq:
        x = dq.popleft()

        for nx in graph[x]:
            if color[nx] == -1:
                color[nx] = 1 - color[x]
                dq.append(nx)

# graph = [ [], [2], [1, 3, 4], [2, 4], [3, 2] ]
# color = [-1, 0, 1, 0, 0]

def Bipartite():
    for idx, dot in enumerate(graph):
        if idx == 0:
            continue

        for ele in dot:
            if color[idx] == color[ele]:
                return False

    return True


ans = []
for _ in range(k):
    V, E = tuple(map(int, input().split()))
    color = [-1] * (V + 1)
    graph = [[] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        u, v = tuple(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)

    bfs(1)

    for i in range(1, V + 1):
        if color[i] == -1:
            bfs(i)
    t1 = Bipartite()

    if t1:
        ans.append("YES")
    else:
        ans.append("NO")

for a in ans:
    print(a)