from collections import deque

n, m = tuple(map(int,input().split()))
maze = [list(map(int,list(input()))) for _ in range(n)]
visited = [ [ [0, 0] for _ in range(m) ] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    dq = deque()
    broken = 0
    dq.append((0, 0, broken))
    visited[0][0][broken] = 1

    while dq:
        x, y, broken = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    dq.append((nx, ny, broken))

                elif maze[nx][ny] == 1 and broken == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][1] = visited[x][y][broken] + 1
                    dq.append((nx, ny, 1))

    return visited[n-1][m-1]

dist = bfs()
if dist[0] == 0 and dist[1] == 0:
    print(-1)
elif dist[0] == 0:
    print(dist[1])
elif dist[1] == 0:
    print(dist[0])
else:
    print(min(dist))
