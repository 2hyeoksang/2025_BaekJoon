n = 1260
cnt = 0
arr = [500, 100, 50, 10]    # arr.sort(reverse = True)

for coin in arr:
    cnt += n // coin
    n = n % coin

print(cnt)