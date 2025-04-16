import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(c_x, c_y):
    dq = deque()
    dq.append((c_x, c_y))
    visited[c_x][c_y] = 1

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if ground[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))


t = int(input())
ans = []
for _ in range(t):
    m, n, k = tuple(map(int, sys.stdin.readline().split()))
    ground = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = tuple(map(int, sys.stdin.readline().split()))
        ground[y][x] = 1

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    ans.append(cnt)

for ele in ans:
    print(ele)