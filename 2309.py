heights = [int(input()) for _ in range(9)]
# [20, 7, 23, 19, 10, 15, 25, 8, 13]

heights.sort()
# [7, 8, 10, 13, 15, 19, 20, 23, 25]

t1 = False
for i in range(9):
    for j in range(8):
        temp = heights.copy()
        sum = 0
        temp.pop(i)
        temp.pop(j)

        for ele in temp:
            sum += ele

        if sum == 100:
            for ele in temp:
                print(ele)
            t1 = True
            break
    if t1:
        break

