
import sys
input = sys.stdin.readline

n = int(input())
a, b, c = tuple(map(int,input().split()))
soldier = list(map(int,input().split()))

def power(x):
    global a, b, c

    return a*(x**2) + b*x + c
    # a*((x + b / 2*a)**2) + c - (b**2 / 4*a)

