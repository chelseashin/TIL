import sys
sys.stdin = open("sum.txt")

T = 10
for tc in range(T):
    N = int(input())
    arr = [[0 for i in range(100)] for j in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    # print(arr)

    max_sum = 0
    # 행
    for i in range(len(arr)):
        row_sum = 0
        for j in range(len(arr[i])):
            row_sum += arr[i][j]
            if max_sum < row_sum:
                max_sum = row_sum
    # 열
    for j in range(len(arr[0])):
        col_sum = 0
        for i in range(len(arr)):
            col_sum += arr[i][j]
            if max_sum < col_sum:
                max_sum = col_sum
    # 대각선 1
    dia_sum_1 = 0
    for i in range(100):
        dia_sum_1 += arr[i][i]
        if max_sum < dia_sum_1:
            max_sum = dia_sum_1
    # 대각선 2
    dia_sum_2 = 0
    for i in range(100):
        dia_sum_2 += arr[i][99-i]
        if max_sum < dia_sum_2:
            max_sum = dia_sum_2

    print(f"{tc + 1} {max_sum}")

