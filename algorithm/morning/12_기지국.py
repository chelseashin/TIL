import sys
sys.stdin = open("기지국.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [["X"] * (N+6) for _ in range(N+6)]
    # arr = [list(map(str, input())) for _ in range(N)]
    for a in range(2, N+3):
        arr[a] = ["X"] * 3 + list(map(str, input())) + ["X"] * 3
    print(arr)

    cnt = 0
    # for i in range(N+6):
    #     for j in range(N+6):
    #         if arr[i][j] == "A":
    #             print(i, j)
    #         elif arr[i][j] == "B":
    #             print(i, j)
    #         elif arr[i][j] == "C":
    #             print(i, j)
    # print(arr)

    Hsum = 0  # 집(H)의 갯수
    for i in range(N + 6):
        for j in range(N + 6):
            if arr[i][j] == "H":
                Hsum += 1

    print("#{} {}".format(tc+1, Hsum))
