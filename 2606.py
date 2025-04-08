from collections import deque
import sys

n = int(input())
k = int(input())
arr = [[] for _ in range(n)]
for _ in range(k):
    u, v = tuple(map(int,sys.stdin.readline().split()))
    arr[u-1].append(v)
    arr[v-1].append(u)

infected = [0 for _ in range(n)]

def bfs(num):
    dq = deque()
    infected[num-1] = 1
    dq.append(num)

    while dq:
        n = dq.popleft()
        new_arr = arr[n-1]
        for ele in new_arr:
            if infected[ele-1] == 0:
                infected[ele-1] = 1
                dq.append(ele)

bfs(1)
cnt = 0
for i in range(1, len(infected)):
    if infected[i] == 1:
        cnt += 1

print(cnt)