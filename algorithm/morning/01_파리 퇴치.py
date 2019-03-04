import sys
sys.stdin = open("파리 퇴치.txt")

# 나의 풀이
# x값, y값이 들어왔을 때
def flies(x, y):
    sum = 0
    for i in range(M):
        for j in range(M):
            sum += data[x+i][y+j]
    return sum

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # print(data)

    total = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            # data[i][j]
            total.append(flies(i, j))

    print("#{} {}".format(tc+1, max(total)))
    
    
# 좋은 풀이 - 최대, 최소 구하기
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
#
#     # 데이터 받는 다른 방법
#     # for i in range(N):
#     #     data[i] = list(map(int, input().split()))
#
#     max = 0
#     min = 987654321
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             sum = 0
#             for x in range(M):
#                 for y in range(M):
#                     sum += data[i+x][j+y]
#             if max < sum:
#                 max = sum
#             if min > sum:
#                 min = sum
#     print(f"#{tc+1} {max} {min}")
