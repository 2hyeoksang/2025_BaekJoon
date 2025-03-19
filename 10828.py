import sys
n = int(input())
arr = []

for _ in range(n):
    order = sys.stdin.readline().rstrip()
    if 'push' in order:
        order1, num = list(order.split())
        num = int(num)
        arr.append(num)

    elif order == 'pop':
        if arr == []:
            print(-1)
            continue

        print(arr.pop(-1))

    elif order == 'size':
        print(len(arr))

    elif order == 'empty':
        if arr == []:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if arr == []:
            print(-1)
            continue

        print(arr[-1])