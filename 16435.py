n, leng = tuple(map(int,input().split()))
fruits = list(map(int,input().split()))
fruits.sort()

for ele in fruits:
    if leng >= ele:
        leng += 1

print(leng)