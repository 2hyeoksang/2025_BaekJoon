t = int(input())
arr = [int(input()) for _ in range(t)]

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


for num in arr:
    if is_prime(num):
        print(0)

    else:
        for i in range(1, num+1):
            if is_prime(num - i):
                first_prime = num - i
                break

        for j in range(1, 1299710):
            if is_prime(num + j):
                sec_prime = num + j
                break

        print(sec_prime - first_prime)