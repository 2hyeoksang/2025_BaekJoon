n, m, k = tuple(map(int,input().split()))
num_arr = list(map(int,input().split()))
# n = 5, m = 8, k = 3
# [2, 4, 5, 4, 6],  6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46

num_arr.sort(reverse = True)
first_num = num_arr[0]
sec_num = num_arr[1]

res = 0
cnt = 0

while True:
    for _ in range(k):
        if cnt == m:
            break
        res += first_num
        cnt += 1
    if cnt == m:
        break
    res += sec_num
    cnt += 1

print(res)
