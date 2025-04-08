from collections import deque
import sys

n, m, r = tuple(map(int, sys.stdin.readline().split()))
arr= [ [] for _ in range(n)]

for _ in range(m):
    u, v = tuple(map(int, sys.stdin.readline().split()))
    arr[u-1].append(v)
    arr[v-1].append(u)

cnt = 1
visited = [0 for _ in range(n)]

def bfs(num):
    global cnt
    visited[num-1] = cnt
    dq = deque()
    dq.append(num)

    while dq:
        n = dq.popleft()
        new_arr = sorted(arr[n-1], reverse= True)
        for ele in new_arr:
            if visited[ele - 1] == 0:
                cnt += 1
                visited[ele - 1] = cnt
                dq.append(ele)

bfs(r)
for ele in visited:
    print(ele)


