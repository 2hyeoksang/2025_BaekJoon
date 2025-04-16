heights = [int(input()) for _ in range(9)]
# [20, 7, 23, 19, 10, 15, 25, 8, 13]

heights.sort()
# [7, 8, 10, 13, 15, 19, 20, 23, 25]

total = sum(heights)
wants = total - 100

t1 = False
for i in range(9):
    for j in range(i+1, 9):
        first = heights[i]
        second = heights[j]

        if first + second == wants:
            f_idx = i
            s_idx = j
            t1 = True
            break

    if t1:
        break

for k in range(9):
    if k == f_idx or k == s_idx:
        continue
    print(heights[k])