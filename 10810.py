n, m = tuple(map(int,input().split()))
arr = [tuple(map(int,input().split())) for _ in range(m)]

backet = [0] * n

for i, j, k in arr:
    for l in range(i - 1, j):
        backet[l] = k

for ele in backet:
    print(ele, end = ' ')