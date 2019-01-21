import sys
sys.stdin = open("sum.txt")       # 표준 입력

T = 10
for tc in range(T):      # testcase
    ans = 0
    N = int(input())
    data = [[0 for i in range(100)] for j in range(100)]
    for i in range(100):
        data[i] = list(map(int, input().split()))
    print(data)
    # print(len(data))  # 각 100개 데이터
    # print(data[1])


row_sum = 0   # 행
col_sum = 0   # 열
dia_sum = 0   # 대각선
for i in range(10):     # data[i]
    for j in range(100):
        if row_sum < sum(data[i][j]):
            row_sum = sum(data[i][j])
            row_sum += sum(data[i][j])

# dia = 0
# for i in range(10):
#     for j in range(10):
#         dia += data[i][j]
# print(dia)

# arr = []
# new = []
# for i in range(100):
#     for j in range(100):
#         new.append(data[i])
#         new.append(data[j])
#     arr.append(new)
# print(new)



    # print("#{} {}".format(tc + 1, ))
