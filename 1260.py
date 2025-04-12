from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m, k = tuple(map(int,sys.stdin.readline().split()))
arr = [[] for _ in range(n)]

for _ in range(m):
    u, v = tuple(map(int,sys.stdin.readline().split()))
    arr[u-1].append(v)
    arr[v-1].append(u)

for i in range(len(arr)):
    arr[i].sort()

d_visited = [0 for _ in range(n)]
b_visited = [0 for _ in range(n)]
d_order = []
b_order = []


def dfs(num):
    d_visited[num - 1] = 1
    d_order.append(num)

    for ele in arr[num-1]:
        if d_visited[ele - 1] == 0:
            dfs(ele)


def bfs(num):
    dq = deque()
    dq.append(num)
    b_visited[num-1] = 1
    b_order.append(num)

    while dq:
        n = dq.popleft()
        for ele in arr[n-1]:
            if b_visited[ele-1] == 0:
                b_visited[ele - 1] = 1
                b_order.append(ele)
                dq.append(ele)


dfs(k)
bfs(k)

for ele in d_order:
    print(ele, end = ' ')
print()
for ele in b_order:
    print(ele, end = ' ')
