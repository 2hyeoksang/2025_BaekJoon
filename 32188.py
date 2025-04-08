from collections import deque
import sys

N, C = tuple(map(int, sys.stdin.readline().split()))

portals = [None] * N
for _ in range(C):
    t, a, b = input().split()
    a = int(a)
    b = int(b)
    portals[a] = (int(b), t)

INF = int(1e9)
dist = [INF] * N
dist[0] = 0

dq = deque()
dq.append(0)

while dq:
    curr = dq.popleft()

    if portals[curr]:
        dest, typ = portals[curr]

        if dist[dest] > dist[curr]:
            dist[dest] = dist[curr]
            dq.appendleft(dest)

        if typ == 'B' and curr + 1 < N:
            if dist[curr + 1] > dist[curr] + 1:
                dist[curr + 1] = dist[curr] + 1
                dq.append(curr + 1)

    elif curr + 1 < N:
        if dist[curr + 1] > dist[curr] + 1:
            dist[curr + 1] = dist[curr] + 1
            dq.append(curr + 1)

print(-1 if dist[N - 1] == INF else dist[N - 1])