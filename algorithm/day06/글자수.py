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
def max_str(str1, str2):
    set(str1) & set(str1)
    ans = 0
    for i in range()
    return ''.join(ans)
T = int(input())
for tc in range(T):
    str1 = input()  # 찾을 패턴
    str2 = input()  # 전체 텍스트
    # print(str1, str2)

    print(f"#{tc + 1} {max_str(str1, str2)}")
