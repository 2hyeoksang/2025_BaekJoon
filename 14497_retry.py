from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(c_x, c_y):
    dq = deque()
    dq.append((c_x, c_y))
    visited[c_x][c_y] = 0

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and  0 <= ny < m:
                if visited[nx][ny] == -1:
                    if arr[nx][ny] == '1' :
                        arr[nx][ny] = '0'
                        visited[nx][ny] = visited[x][y] + 1
                        dq.append((nx, ny))

                    elif arr[nx][ny] == '#' :
                        print(visited[x][y] + 1)
                        return

                    else:
                        visited[nx][ny] = visited[x][y]
                        dq.appendleft((nx, ny))


n, m = tuple(map(int,input().split()))
Jx, Jy, Bx, By = tuple(map(int,input().split()))

arr = [list(input()) for _ in range(n)]
visited = [ [-1] * m for _ in range(n)]

bfs(Jx-1, Jy-1)