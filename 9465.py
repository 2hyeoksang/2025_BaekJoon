import sys

input = sys.stdin.readline

t = int(input())


def find(m, n):
    if n == 0:
        val = arr[m][n]

    elif n == 1:
        if m == 0:
            val = dp[1][n-1] + arr[m][n]
        else:
            val = dp[0][n-1] + arr[m][n]

    else:
        if m == 0:
            val = max(dp[0][n-2] + arr[m][n], dp[1][n-2] + arr[m][n], dp[1][n-1] + arr[m][n])
        else:
            val = max(dp[0][n-2] + arr[m][n], dp[1][n-2] + arr[m][n], dp[0][n-1] + arr[m][n])

    return val


ans = []
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    for i in range(n):
        for j in range(2):
            dp[j][i] = find(j, i)

    ans.append(max(map(max, dp)))

for ele in ans:
    print(ele)