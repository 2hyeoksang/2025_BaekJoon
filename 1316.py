n = int(input())

arr = [input() for _ in range(n)]

def is_group(word):
    letter = list(word)
    leng = len(letter)
    for i in range(leng-1):
       for j in range(i+2, leng):
           if letter[i] != letter[i+1] and letter[i] == letter[j]:
               return False

    return True

cnt = 0
for word in arr :
    if is_group(word):
        cnt+=1

print(cnt)