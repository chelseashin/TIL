import sys
sys.stdin = open("05.txt")

# 나의 풀이 - 그리디 방법
N = int(input())
Z = list(map(int, input().split()))
Z.sort()    # 오르차순 정렬한 예산
# print(Z)
M = int(input())

# ans = 0
# if sum(Z) <= M:
#     ans = max(Z)
# else:
#     sum = 0
#     for i in range(N):
#         if Z[i] * (N-i) <= (M-sum):    # 현재 예산액으로 배정 가능하면
#             sum += Z[i]
#         else:    # 현재 예산액으로 배정 불가능
#             ans = int((M-sum) // (N-i))
#             break
# print(ans)


# 다른 풀이 - 이진탐색
# N, arr, M
def check(m):
    # 상한액으로 지방에서 요청액을 배정 락능하면 배정하고 아니면 상한액으로 합계 계산
    tot = 0
    for i in range(N):
        if Z[i] <= m:
            tot += Z[i]
        else: tot += m
    # 합계가 총액 이하이면 성공 아니면 실패 리턴
    if tot <= M: return 1
    else: return 0

e = max(Z)
s = 1
sol = 0
while s <= e:
    m = (s+e) // 2
    if check(m):    # 성공하면 상한액을 늘리고
        sol = m
        s = m+1
    else:           # 초과하면 상한액을 줄임
        e = m-1
print(sol)