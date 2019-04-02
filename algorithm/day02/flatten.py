import sys
sys.stdin = open("flatten.txt")       # 표준 입력

T = 10
for tc in range(T):      # testcase
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)
    # print(len(data))  # 각 100개 데이터

    for i in range(N):
        max_h = data[0]
        min_h = data[0]

        max_idx = 0
        min_idx = 0

        for j in range(len(data)):
            if data[j] >= max_h:
                max_h = data[j]
                max_idx = j
            if data[j] <= min_h:
                min_h = data[j]
                min_idx = j

        data[max_idx] -= 1
        data[min_idx] += 1

    print("#{} {}".format(tc+1, max(data) - min(data)))


    # 다른 쉬운 풀이
    # for i in range(N):
    #     max_data, min_data = max(data), min(data)
    #     max_idx, min_idx = data.index(max_data), data.index(min_data)
    #     data[max_idx] -= 1
    #     data[min_idx] += 1
    # print("#{} {}".format(tc + 1, max(data) - min(data)))