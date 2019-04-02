import sys
sys.stdin = open("기지국.txt")

def Asum(x, y):
    global arr
    a = 0
    if arr[x-1][y] == "H":
        a += 1
        arr[x-1][y] = "X"
    elif arr[x+1][y] == "H":
        a += 1
        arr[x+1][y] = "X"
    elif arr[x][y-1] == "H":
        a += 1
        arr[x][y-1] = "X"
    elif arr[x][y+1] == "H":
        a += 1
        arr[x][y+1] = "X"
    return a

def Bsum(x, y):
    global arr
    b = 0
    if arr[x - 1][y] == "H":
        b += 1
        arr[x - 1][y] = "X"
    elif arr[x + 1][y] == "H":
        b += 1
        arr[x + 1][y] = "X"
    elif arr[x][y - 1] == "H":
        b += 1
        arr[x][y - 1] = "X"
    elif arr[x][y + 1] == "H":
        b += 1
        arr[x][y + 1] = "X"
    elif arr[x - 2][y] == "H":
        b += 1
        arr[x - 2][y] = "X"
    elif arr[x + 2][y] == "H":
        b += 1
        arr[x + 2][y] = "X"
    elif arr[x][y - 2] == "H":
        b += 1
        arr[x][y - 2] = "X"
    elif arr[x][y + 2] == "H":
        b += 1
        arr[x][y + 2] = "X"
    return b

def Csum(x, y):
    global arr
    c = 0
    if arr[x - 1][y] == "H":
        c += 1
        arr[x - 1][y] = "X"
    elif arr[x + 1][y] == "H":
        c += 1
        arr[x + 1][y] = "X"
    elif arr[x][y - 1] == "H":
        c += 1
        arr[x][y - 1] = "X"
    elif arr[x][y + 1] == "H":
        c += 1
        arr[x][y + 1] = "X"
    elif arr[x - 2][y] == "H":
        c += 1
        arr[x - 2][y] = "X"
    elif arr[x + 2][y] == "H":
        c += 1
        arr[x + 2][y] = "X"
    elif arr[x][y - 2] == "H":
        c += 1
        arr[x][y - 2] = "X"
    elif arr[x][y + 2] == "H":
        c += 1
        arr[x][y + 2] = "X"

    elif arr[x - 3][y] == "H":
        c += 3
        arr[x - 3][y] = "X"
    elif arr[x + 3][y] == "H":
        c += 1
        arr[x + 3][y] = "X"
    elif arr[x][y - 3] == "H":
        c += 1
        arr[x][y - 3] = "X"
    elif arr[x][y + 3] == "H":
        c += 1
        arr[x][y + 3] = "X"
    return c



T = int(input())
for tc in range(T):
    N = int(input())
    arr = [["X"] * (N+6) for _ in range(N+6)]
    # arr = [list(map(str, input())) for _ in range(N)]
    for a in range(3, N+3):
        arr[a] = ["X"] * 3 + list(map(str, input())) + ["X"] * 3
    # print(arr)

    Hsum = 0     # 집(H)의 갯수
    for i in range(N+6):
        for j in range(N+6):
            if arr[i][j] == "H":
                Hsum += 1
    # print(Hsum)
    cnt = 0
    for i in range(N+6):
        for j in range(N+6):
            if arr[i][j] == "A":
                cnt += Asum(i, j)
            elif arr[i][j] == "B":
                cnt += Bsum(i, j)
            elif arr[i][j] == "C":
                cnt += Csum(i, j)
    print(arr)

    # print("#{} {}".format(tc+1, Hsum-cnt))
