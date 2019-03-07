import sys
sys.stdin = open("소수.txt")

T = 3
for i in range(T):
    a, b = map(int, input().split())    # 2, 10
    sosu = [0]*100

    smin = 987654321
    smax = 0
    for i in range(a, b+1):
        if i*i > 100: break
        if sosu[i]:
            continue
        for j in range(i*2, 101, i):
            sosu[j] = 1