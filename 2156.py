n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [-1 for _ in range(n)]

def find(n):
    if n == 0:
        val = wines[0]

    elif n == 1:
        val = wines[n] + dp[n-1]

    elif n == 2:
        val = max(dp[n-1], dp[n-2] + wines[n], wines[n] + wines[n-1])

    else:
        val = max(dp[n-1], dp[n-2] + wines[n], dp[n-3] + wines[n] + wines[n-1])

    return val


for i in range(n):
    dp[i] = find(i)

print(dp[n-1])
