import sys
sys.stdin = open("sum.txt")       # 표준 입력

T = 10
for tc in range(T):      # testcase
    N = int(input())
    data = [[0 for i in range(100)] for j in range(100)]
    for i in range(100):
        data[i] = list(map(int, input().split()))
    # print(data)
    # print(len(data))  # 각 100개 데이터 * 10(tc)

    # 행
    row_max = 0
    for i in range(len(data)):
        row_sum = 0
        for j in range(len(data[i])):
            row_sum += data[i][j]
            if row_max < row_sum:
                row_max = row_sum

    # 열
    col_max = 0
    for j in range(len(data[0])):
        col_sum = 0
        for i in range(len(data)):
            col_sum += data[i][j]
            if col_max < col_sum:
                col_max = col_sum

    # 대각선(\)
    dia_max_1 = 0
    for i in range(len(data)):
        dia_sum_1 = 0
        dia_sum_1 += data[i][i]
        if dia_max_1 < dia_sum_1:
            dia_max_1 = dia_sum_1

    # 대각선 (/)
    dia_max_2 = 0
    for i in range(len(data)):
        dia_sum_2 = 0
        dia_sum_2 += data[i][100-i-1]
        if dia_max_2 < dia_sum_2:
            dia_max_2 = dia_sum_2

    ans = max(row_max, col_max, dia_max_1, dia_max_2)

    print("#{} {}".format(tc + 1, ans))


