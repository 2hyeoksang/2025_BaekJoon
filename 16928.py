from collections import deque
import sys

input = sys.stdin.readline

n, m = tuple(map(int,input().split()))

ladder = [tuple(map(int,input().split())) for _ in range(n)]
snake = [tuple(map(int,input().split())) for _ in range(m)]

dices = [1, 2, 3, 4, 5, 6]

visited = [-1 for _ in range(0, 101)]
ans = []

def bfs():
    dq = deque()
    dq.append(1)
    visited[1] = 0

    while dq:
        pos = dq.popleft()
        for i in range(6):
            next_pos = pos + dices[i]

            if next_pos <= 100 and visited[next_pos] == -1:
                for x, y in ladder:
                    if next_pos == x:
                        visited[next_pos] = visited[pos] + 1
                        next_pos = y

                for z, k in snake:
                    if next_pos == z:
                        visited[next_pos] = visited[pos] + 1
                        next_pos = k

                if visited[next_pos] == -1:
                    visited[next_pos] = visited[pos] + 1
                    dq.append(next_pos)


bfs()
print(visited[100])