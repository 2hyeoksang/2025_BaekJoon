import sys

n = int(input())
weight = []
for i in range(n):
    weight.append(int(sys.stdin.readline()))

weight.sort()
# [10, 15, 20, 25]  ->  얘는 답이 45
max_val = 0

for i in range(n):
    max_val = max(max_val, weight[i] * (n - i))

print(max_val)