import sys
sys.stdin = open("과수원.txt")

N = int(input())
farm = [list(map(int, input())) for _ in range(N)]

# 사과 개수 구하는 함수
def apple_count(x, y):
    balance = 0
    apple1 = 0
    for i in range(x):
        for j in range(y):
            if farm[i][j] == 1:
                apple1 += 1
    apple2 = 0
    for i in range(x):
        for j in range(y, N):
            if farm[i][j] == 1:
                apple2 += 1
    apple3 = 0
    for i in range(x, N):
        for j in range(y):
            if farm[i][j] == 1:
                apple3 += 1

    apple4 = 0
    for i in range(x, N):
        for j in range(y, N):
            if farm[i][j] == 1:
                apple4 += 1

    if apple1 == apple2 == apple3 == apple4:
        balance = 1

    return balance

sol = 0         # 각 사분면의 사과 개수가 균등한 케이스 총 몇 개인지
for i in range(1, N):
    for j in range(1, N):
        sol += apple_count(i, j)    # 각 사분면의 사과 개수가 균등한지 1, 0

# 균등한 케이스 없는 경우에는 -1
if sol == 0:
    sol = -1

print(sol)