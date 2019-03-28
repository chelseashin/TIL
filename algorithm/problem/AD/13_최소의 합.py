import sys
sys.stdin = open("13.txt")

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# chk = [0]*n
# rec = [0]*n
#
# # 중복 가능한 0~2순열 (중복순열)
# def dfs2(no, a, b):
#     global sums
#     if b>=sums:
#         return
#     if no>=n:
#         sums = min(sums, b)
#         return
#     for i in range(n):
#         rec[no] = i
#         dfs2(no+1, a+1, b+arr[a][i])
#
#
# # 중복 없는 0~2 순열 (순열)
# def dfs(no, a, b):
#     global sums
#     if b>=sums:
#         return
#     if no>=n:
#         sums = min(sums, b)
#         return
#     for i in range(n):
#         if chk[i]:
#             continue
#         chk[i] = 1
#         rec[no] = i
#         dfs(no+1, a+1, b+arr[a][i])
#         chk[i] = 0
#
#
# sums=float('inf')
# dfs2(0, 0, 0)
# print(sums)
# sums=float('inf')
# dfs(0, 0, 0)
# print(sums)

# 좋은 풀이
def DFS1(no, nsum):  # 현재 행에서 모든 열을 사용하는 경우의 수
    global nmin
    if nsum > nmin:
        return
    if no >= N:   # no: depth
        # for i in range(N):
        #     print(rec[i], end=' ')
        # print(nsum)
        if nsum < nmin:
            nmin = nsum
        return
    for i in range(N):  # 열
        rec[no] = arr[no][i]    # 고른 값을 기록
        DFS1(no+1, nsum + arr[no][i])

def DFS2(no, nsum):
    global nmin
    if nsum > nmin:
        return
    if no >= N:
        # for i in range(N):
        #     print(rec[i], end=' ')
        # print(nsum)
        if nsum < nmin:
            nmin = nsum
        return
    for i in range(N):
        if chk[i]:
            continue
        chk[i] = 1
        rec[no] = arr[no][i]    # 고른 값을 기록
        DFS2(no+1, nsum+arr[no][i])
        chk[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

rec = [0] * N   # 고른 값을 기록배열(디버깅용)
chk = [0] * N   # 열 체크배열

# 첫번째 방법 : 열의 중복을 허용한 중복순열
nmin = 987654321
DFS1(0, 0)   # 0행부터 시작, 합계는 0
print(nmin)

# 두번째 방법 : 열의 중복을 배제한 순열
nmin = 987654321
DFS2(0, 0)
print(nmin)
