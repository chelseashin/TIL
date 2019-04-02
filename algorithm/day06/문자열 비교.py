import sys
sys.stdin = open("문자열 비교.txt")

# 나의 풀이(in 메소드 사용)
# T = int(input())
# for tc in range(T):
#     str1 = input()     # 찾을 패턴
#     str2 = input()     # 전체 텍스트
#     N = len(str1)      # 찾을 패턴의 길이 : 4 4 12
#     M = len(str2)      # 전체 텍스트의 길이 : 10 10 20
#     if str1 in str2:
#         ans = 1
#     else:
#         ans = 0
#
#     print(f"#{tc + 1} {ans}")

# 나의 풀이 2
T = int(input())
for tc in range(T):
    S1 = input()
    S2 = input()
    N, M = len(S1), len(S2)

    ans = 0
    for i in range(M-N+1):
        cnt = 0
        for j in range(N):
            if S1[j] == S2[i+j]:
                cnt += 1
        if cnt == N:
            ans = 1

    print("#{} {}".format(tc+1, ans))

# 두번째 풀이
# def BruteForce(str1, str2):
#     i = 0  # str1의 인덱스
#     j = 0  # str2의 인덱스
#     N = len(str1)      # 찾을 패턴의 길이 : 4 4 12
#     M = len(str2)      # 전체 텍스트의 길이 : 10 10 20
#     while j < N and i < M:
#         if str2[i] != str1[j]:
#             i = i - j
#             j = -1
#         i += 1
#         j += 1
#     if j == N:
#         return 1   # 검색 성공
#     else:
#         return 0  # 검색 실패
# T = int(input())
# for tc in range(T):
#     str1 = input()     # 찾을 패턴
#     str2 = input()     # 전체 텍스트
#
#     print(f"#{tc + 1} {BruteForce(str1, str2)}")


# 세번째 풀이
# def my_str(str1, str2):
#     for i in range(len(str2)):
#         if str2[i:i+len(str1)] == str1:
#             return 1
#     return 0
#
# T = int(input())
# for tc in range(T):
#     str1 = input()     # 찾을 패턴
#     str2 = input()     # 전체 텍스트
#
#     print(f"#{tc + 1} {my_str(str1, str2)}")
