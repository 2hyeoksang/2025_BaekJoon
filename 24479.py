import sys
sys.setrecursionlimit(10**6)

def dfs(num):
    global cnt
    # visited[num - 1] = 1
    order[num - 1] = cnt
    new_arr = sorted(arr[num-1], reverse = True)    # 24480 할 때는 reverse = True 추가
    # print(cnt)
    for idx in new_arr:
        if order[idx - 1] == 0 :
            cnt += 1
            dfs(idx)


n, m, r = tuple(map(int,sys.stdin.readline().split()))
arr = [[] for _ in range(n)]
# visited = [0] * n
order =[0] * n
cnt = 1

for _ in range(m):
    u, v = tuple(map(int,sys.stdin.readline().split()))
    arr[u-1].append(v)
    arr[v-1].append(u)
# arr = [[4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]

dfs(r)

for i in order:
    print(i)