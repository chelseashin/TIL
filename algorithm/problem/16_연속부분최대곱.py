import sys
sys.stdin = open("연속부분최대곱.txt")

N = int(input())
arr = [float(input()) for _ in range(N)]
# print(L)

# 다시 풀기
# 이중 for문
# Max = 0.0    # 최댓값
# for i in range(N):
#     mul = 1        # 누적곱
#     for j in range(i, N):
#         mul *= arr[j]
#         if Max < mul:
#             Max = mul
#
# print(format(Max, '.3f'))


# 1개의 for문
mul = 1
Max = 0.0
for i in range(N):
    mul *= arr[i]
    if mul < arr[i]:
        mul = arr[i]
    if Max < mul:
        Max = mul
print(format(Max, '.3f'))


# 나의 풀이
# N = int(input())
# L = [float(input()) for _ in range(N)]
# new = [0] * N
# new[0] = L[0]
#
# for i in range(1, N):
#     if new[i-1] * L[i] > L[i]:
#         new[i] = new[i-1] * L[i]
#     else:
#         new[i] = L[i]
# ans = max(new)
#
# print(format(ans, '.3f'))