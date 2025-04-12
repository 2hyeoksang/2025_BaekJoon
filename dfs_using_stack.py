import sys

n, m, r = tuple(map(int,sys.stdin.readline().split()))
arr = [ [] for _ in range(n)]
for _ in range(m):
    u, v = tuple(map(int,sys.stdin.readline().split()))
    arr[u-1].append(v)
    arr[v-1].append(u)

visited = [0 for _ in range(n)]
cnt = 1

for i in range(n):
    arr[i].sort()

def dfs(num):
    global cnt
    visited[num-1] = cnt
    stack = []
    stack.append(num)

    while stack:
        n = stack[-1]
        found = False
        for ele in arr[n-1]:
            if visited[ele-1] == 0:
                cnt += 1
                visited[ele-1] = cnt
                stack.append(ele)
                found = True
                break

        if not found:
            stack.pop()

dfs(r)
# for ele in visited:
#     print(ele)

ans = "\n".join(map(str, visited))
print(ans)