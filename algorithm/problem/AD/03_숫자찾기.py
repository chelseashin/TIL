import sys
sys.stdin = open("03.txt")

# 이진탐색
def binarySearch(a, k):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (start + end) // 2
        if k == a[middle]:    # 검색 성공
            return middle+1
        elif k < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return 0

N = int(input())
num = list(map(int, input().split()))
T = int(input())
t = list(map(int, input().split()))

for i in t:
    print(binarySearch(num, i))

# time error 1
# for i in range(T):
#     ans = 0
#     for j in range(N):
#         if t[i] == num[j]:
#             ans = j+1
#     print(ans)

# time error 2
# for i in range(T):
#     idx = 0
#     for j in range(N):
#         if t[i] in num:
#             idx = num.index(t[i]) + 1
#     print(idx)