import sys
sys.stdin = open("회문.txt")


def my_palindrome(data, N, M):
    for i in range(N):
        for j in range(N-M+1):  # range 함수 써야하기 때문에 +1 해줌
            flag = 1
            for k in range(M//2):
                if data[i][j+k] != data[i][j+M-1-k]:  # M-1 : 마지막 인덱스를 나타냄
                    flag = 0
                    break
            if flag:
                for l in range(M):
                    print(data[i][j+l] , end="")


    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if data[j+k][i] != data[j+M-1-k][i]:
                    flag = 0
                    break
            if flag:
                for l in range(M):
                    print(data[j+l][i], end="")

T = int(input())
for tc in range(T):      # testcase
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    # print(N, M)
    # print(data)
    # print(len(data))    # 10 10 20


    print(f"#{tc + 1}", end=" ")
    my_palindrome(data, N, M)
    print()

# 나의 풀이 - 다시 풀어보기
# def my_palindrome(data):
#     for i in range(len(data)):
#         if data[i:i+M] == data[:-M-1:-1]:
#             ans = data[i:i+M]
#             return ans

# T = int(input())
# for tc in range(T):      # testcase
#     N, M = map(int, input().split())
#     data = [input() for _ in range(N)]
#
# rev = [[0 for i in range(N)] for j in range(N)]
#     for j in range(N):
#         for i in range(N):
#             rev[i][j] = data[j][i]
#     # print(rev)
#     # print(len(rev))    # 10 10 20
#
#     list_rev = []
#     for i in range(len(rev)):
#         list_rev.append(''.join(rev[i]))
#     # print(list_rev)

# print(f"#{tc + 1} {my_palindrome(list_rev, N)}")