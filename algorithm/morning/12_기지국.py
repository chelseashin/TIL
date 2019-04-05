import sys
sys.stdin = open("기지국.txt")

def coverA(x, y):
    for i in range(1, 2):   # 벽 고려하여 범위 주기
        if x + i < N and arr[x+i][y] == "H":
            arr[x+i][y] = "X"
        if y + i < N and arr[x][y+i] == "H":
            arr[x][y+i] = "X"
        if x - i >= 0 and arr[x-i][y] == "H":
            arr[x-i][y] = "X"
        if y - i >= 0 and arr[x][y-i] == "H":
            arr[x][y-i] = "X"

def coverB(x, y):
    for i in range(1, 3):
        if x + i < N and arr[x+i][y] == "H":
            arr[x+i][y] = "X"
        if y + i < N and arr[x][y+i] == "H":
            arr[x][y+i] = "X"
        if x - i >= 0 and arr[x-i][y] == "H":
            arr[x-i][y] = "X"
        if y - i >= 0 and arr[x][y-i] == "H":
            arr[x][y-i] = "X"

def coverC(x, y):
    for i in range(1, 4):
        if x + i < N and arr[x+i][y] == "H":
            arr[x+i][y] = "X"
        if y + i < N and arr[x][y+i] == "H":
            arr[x][y+i] = "X"
        if x - i >= 0 and arr[x-i][y] == "H":
            arr[x-i][y] = "X"
        if y - i >= 0 and arr[x][y-i] == "H":
            arr[x][y-i] = "X"

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    # print(arr)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "A":
                coverA(i, j)
            elif arr[i][j] == "B":
                coverB(i, j)
            elif arr[i][j] == "C":
                coverC(i, j)
    print(arr)

    Hsum = 0  # 집(H)의 갯수
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "H":
                Hsum += 1

    print("#{} {}".format(tc+1, Hsum))
