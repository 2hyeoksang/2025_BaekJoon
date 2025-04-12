import sys

n = int(sys.stdin.readline())
dots = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
dots.sort()

for x, y in dots:
    print(x, y)