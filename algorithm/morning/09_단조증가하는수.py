import sys
sys.stdin = open('단조증가하는수.txt')

def danjo(x):
    t = x % 10    # 10으로 나눈 나머지
    x //= 10      # 10으로 나눈 몫
    while x:
        if x % 10 > t:
            return False
        t = x % 10
        x //= 10
    return True


T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    #

    max_mul = -1    # 가장 큰 곱
    for i in range(N):
        mul = 0     # 케이스별 곱
        for j in range(i, N):
            if i != j:
                mul = data[i] * data[j]
                if danjo(mul):    # 단조이면
                    if max_mul < mul:
                        max_mul = mul

    print("#{} {}".format(tc+1, max_mul))


# 다른 풀이
# def solve(x):
#     t = x % 10
#     x //= 10
#     while x:
#         if x % 10 > t:
#             return False
#         t = x % 10
#         x //= 10
#         return True
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#
#     rst = -1
#     for i in range(N-1):
#         for j in range(i+1, N):
#             num = data[i]
#             if solve(num):
#                 if rst < num:
#                     rst = num
#
#     print("#{} {}".format(tc+1, rst))