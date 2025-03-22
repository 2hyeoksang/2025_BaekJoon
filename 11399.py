n = int(input())
times = list(map(int, input().split()))
# [3, 1, 4, 3, 2]
#  1  2  3  4  5
times.sort()
# [1, 2, 3, 3, 4]
#  2  5  1  4  3
ans = 0
for i in range(len(times)):
    ans += times[i] * (n - i)

print(ans)