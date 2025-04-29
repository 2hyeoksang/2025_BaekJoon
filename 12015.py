n = int(input())

seq = list(map(int, input().split()))
sub = []
sub.append(seq[0])

def find(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] >= target:
            right = mid

        else:
            left = mid + 1

    return (left + right) // 2

for i in range(1, n):
    if seq[i] > sub[-1]:
        sub.append(seq[i])

    else:
        idx = find(sub, seq[i])
        sub[idx] = seq[i]


print(len(sub))

