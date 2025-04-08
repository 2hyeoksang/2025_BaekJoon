from collections import deque

n, m = tuple(map(int,input().split()))
jooX, jooY, bX, bY = tuple(map(int,input().split()))
arr = []
for _ in range(n):
    arr.append(list(input()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[-1] * m for _ in range(n)]


def bfs(s_x,s_y):
    dq = deque()
    dq.append((s_x, s_y))
    visited[s_x][s_y] = 0

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    if arr[nx][ny] == '1':
                        visited[nx][ny] = visited[x][y] + 1
                        dq.append((nx, ny))

                    elif arr[nx][ny] == '#':
                        print(visited[x][y] + 1)
                        return

                    else :
                        visited[nx][ny] = visited[x][y]
                        dq.appendleft((nx,ny))

bfs(jooX - 1, jooY - 1)