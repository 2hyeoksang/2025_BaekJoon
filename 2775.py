t = int(input())
arr = []
for _ in range(t):
    k = int(input())
    n = int(input())
    arr.append((k,n))

for k, n in arr:
    zero_floor = [i for i in range(1,n+1)]  # [1, 2, 3]

    for _ in range(k):
        next_floor = []
        for j in range(n):  # j = 0, 1, 2
            next_floor.append(sum(zero_floor[:j+1]))  #next_floor = [1, 3, 6]
        zero_floor = next_floor # zero_floor = [1, 3, 6]

    print(zero_floor[n-1])