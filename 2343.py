n, m = tuple(map(int,input().split()))
arr = list(map(int,input().split()))
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
time_min = max(arr)     # 9
time_max = sum(arr)     # 45
# time = [i for i in range(time_min, time_max + 1)]

def separate(num):
    global m
    sum_val = 0
    cnt = 1

    for i in range(n):
        sum_val += arr[i]

        if sum_val > num:
            sum_val = arr[i]
            cnt += 1

    if cnt <= m:
        return True
    else:
        return False

left, right = time_min, time_max
ans = []

while left <= right:
    mid = (left + right) // 2
    t1 = separate(mid)

    if t1:
        ans.append(mid)
        right = mid - 1
    else:
        left = mid + 1

print(min(ans))