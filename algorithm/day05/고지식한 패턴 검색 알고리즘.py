p = "is"    # 찾을 패턴
t = "This is a book~!"    # 전체 텍스트
M = len(p)    # 찾을 패턴의 길이
N = len(t)    # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0     # t의 인덱스
    j = 0     # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M :
        return i - M   # 검색 성공
    else:
        return -1    # 검색 실패

print(BruteForce(p, t))   # p가 t에 2번째에 처음으로 나온다!


# 다른 방법
# def bruteForce2(text, pattern):
#     for i in range(len(text)-len(pattern)+1):
#         cnt = 0
#         for j in range(len(pattern)):
#             if text[i+j] != pattern[j]:
#                 break
#             else:
#                 cnt += 1
#         if(cnt >= len(pattern)):
#             return i
#
# print(bruteForce2(p, t))