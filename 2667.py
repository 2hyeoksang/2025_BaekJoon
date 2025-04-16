from collections import deque

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
h_set = []

def bfs(c_x, c_y):
    dq = deque()
    dq.append((c_x, c_y))
    visited[c_x][c_y] = 1
    h_cnt = 1

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    dq.append((nx, ny))
                    visited[nx][ny] = 1
                    h_cnt += 1

    h_set.append(h_cnt)



cnt = 0
for x in range(n):
    for y in range(n):
        if arr[x][y] == 1 and visited[x][y] == 0:
            bfs(x,y)
            cnt += 1

h_set.sort()

print(cnt)
for ele in h_set:
    print(ele)