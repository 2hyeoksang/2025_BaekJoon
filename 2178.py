from collections import deque

n, m = tuple(map(int,input().split()))
maze = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(c_x, c_y):
    dq = deque()
    dq.append((c_x, c_y))
    visited[c_x][c_y] = 1

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    dq.append((nx, ny))


bfs(0, 0)
print(visited[n-1][m-1])
