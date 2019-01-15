import sys
sys.stdin = open("flatten.txt")       # 표준 입력

T = 10
for tc in range(T):      # testcase
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)
    # print(len(data))  # 각 100개 데이터

    for i in range(N):
        Max = data[0]
        Min = data[0]

        Max_index = 0
        Min_index = 0

        for i in range(len(data)):

            if Max < data[i]:
                Max = data[i]
                Max_index = i

            if data[i] < Min:
                Min = data[i]
                Min_index = i

        data[Max_index] -= 1
        data[Min_index] += 1

    print("#{} {}".format(tc + 1, max(data) - min(data)))
