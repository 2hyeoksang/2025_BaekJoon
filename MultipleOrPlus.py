num = list(map(int,list(input())))

res = num[0]

for ele in num:
    if ele == 0 or ele == 1:
        res += ele
    else:
        res *= ele

print(res)