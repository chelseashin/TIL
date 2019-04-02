import sys
sys.stdin = open("글자수.txt")

# def how_many(str1, str2):
#
#     max_str = 0
#     for i in str1:
#         cnt = 0
#         for j in str2:
#             if i == j:
#                 cnt += 1
#         if max_str < cnt:
#             max_str = cnt
#     return max_str
#
# T = int(input())
# for tc in range(T):
#     str1 = input()  # 찾을 패턴
#     str2 = input()  # 전체 텍스트
#
#     print(f"#{tc + 1} {how_many(str1, str2)}")
#


# 다른 풀이

T = int(input())
for tc in range(T):
    S1 = input()
    S2 = input()
    N, M = len(S1), len(S2)

    L = [0] * N

    for i in range(M):
        if S2[i] in S1:
            L[S1.index(S2[i])] += 1
    print("#{} {}".format(tc+1, max(L)))

