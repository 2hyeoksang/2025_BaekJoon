from collections import deque

m, n = tuple(map(int,input().split()))

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

visited = [[-1] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
     dq = deque()

     for i in range(n):
         for j in range(m):
             if arr[i][j] == 1:
                 dq.append((i, j))
                 visited[i][j] = 0

     while dq:
         x, y = dq.popleft()
         for k in range(4):
             nx, ny = x + dx[k], y + dy[k]
             if 0 <= nx < n and 0 <= ny < m:
                 if arr[nx][ny] == 0:
                     arr[nx][ny] = 1
                     visited[nx][ny] = visited[x][y] + 1
                     dq.append((nx, ny))

bfs()

t1 = False
for ele in arr:
    if 0 in ele:
        t1 = True
        break

if t1:
    print(-1)
else:
    print(max(map(max,visited)))