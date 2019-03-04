import sys
sys.stdin = open("회전.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    num = M % N
    print("#{} {}".format(tc + 1, data[num]))


# 숫자 단위로 풀어보기 - 나중에 해보자
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     data = list(map(str, input().split()))
#     # print(N, M)
#     # print(data)
#
#     total = 0
#     new = []
#     for i in range(N):
#         for j in range(len(data[i])):
#             new.append(int(data[i][j]))
#             total += 1
#     print(new)    # 숫자 리스트 형태
#     print(total)  # 리스트의 길이
