from collections import deque

n, k = tuple(map(int,input().split()))
visited = [-1] * 100001


def bfs(num):
    dq = deque()
    dq.append(num)
    visited[num] = 0

    while dq:
        x = dq.popleft()
        arr = [x-1, x+1, x*2]

        for ele in arr:
            if 0 <= ele <= 100000:
                if visited[ele] == -1:
                    visited[ele] = visited[x] + 1
                    dq.append(ele)


bfs(n)
print(visited[k])
