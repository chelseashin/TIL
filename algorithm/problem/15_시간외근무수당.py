import sys
sys.stdin = open("시간외근무수당.txt")

N = 5
# L = []
# for i in range(5):
#     L.append(list(map(float, input().split())))
L = [list(map(float, input().split())) for _ in range(5)]
# print(L)

time = 0
for i in range(N):
    if L[i][1]-L[i][0] <= 1:
        time += 0
    elif L[i][1]-L[i][0] >= 5:
        time += 4
    else:
        time += L[i][1]-L[i][0] - 1
# print(time)

if time >= 15:
    print(int(time * 10000 * 0.95))
elif time <= 5:
    print(int(time * 10000 * 1.05))
else:
    print(int(time * 10000))