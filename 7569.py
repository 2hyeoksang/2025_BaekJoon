import sys
from collections import deque

input = sys.stdin.readline

m, n, k = tuple(map(int,input().split()))
tomato = []
visited = [ [[-1] * m for _ in range(n)] for _ in range(k) ]

for _ in range(k):
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    tomato.append(arr)  # 어차피 1,2,3층 반대로 뒤집어도 전이되는건 마찬가지


dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0 ,0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    dq = deque()

    for i in range(k):
        for j in range(n):
            for l in range(m):
                if tomato[i][j][l] == 1:
                    dq.append((i, j, l))
                    visited[i][j][l] = 0

    while dq:
        z, x, y = dq.popleft()

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0 <= nz < k and 0 <= nx < n and 0 <= ny < m:
                if tomato[nz][nx][ny] == 0 and visited[nz][nx][ny] == -1:
                    dq.append((nz, nx, ny))
                    tomato[nz][nx][ny] = 1
                    visited[nz][nx][ny] = visited[z][x][y] + 1

bfs()
# print(tomato)
# print(visited)
t1 = True
max_val = -100

for i in range(k):
    for j in range(n):
        for l in range(m):
            if tomato[i][j][l] == 0:
                t1 = False
                break
            if visited[i][j][l] >= max_val:
                max_val = visited[i][j][l]

if t1:
    print(max_val)
else:
    print(-1)


