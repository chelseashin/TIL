import sys
sys.stdin = open("flatten.txt")

T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
#     # print(data)
#
#     for i in range(N):
#
#         hmax = 0  # 최고점
#         hmin = 987654321  # 최저점
#         max_idx = 0   # 최대일 때 인덱스
#         min_idx = 0   # 최소일 때 인덱스
#
#         for j in range(len(data)):
#             if data[j] > hmax:
#                 hmax = data[j]
#                 max_idx = j
#
#             if data[j] < hmin:
#                 hmin = data[j]
#                 min_idx = j
#
#         data[max_idx] -= 1
#         data[min_idx] += 1
#
#     print("#{} {}".format(tc+1, max(data)-min(data)))

# 다른풀이 - 훨씬 간단함
    for i in range(N):
        max_data, min_data = max(data), min(data)
        max_idx, min_idx = data.index(max_data), data.index(min_data)
        data[max_idx] -= 1
        data[min_idx] += 1
    print("#{} {}".format(tc + 1, max(data) - min(data)))