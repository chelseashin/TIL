import sys
sys.stdin = open("연속부분최대곱.txt")

N = int(input())
L = [float(input()) for _ in range(N)]

new = [0] * N
new[0] = L[0]

for i in range(1, N):
    if new[i-1] * L[i] > L[i]:
        new[i] = new[i-1] * L[i]
    else:
        new[i] = L[i]
ans = max(new)

print(format(ans, '.3f'))