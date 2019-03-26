# def bino(n, k):
#     B = [[0] * n for _ in range(k)]
#     for i in n:
#         for j in k:
#             if j == 0 or j == i:
#                 B[i][j] = 1
#             else:
#                 B[i][j] = B[i-1][j-1] + B[i-1][j]
#
#     return B[n][k]

# 순열 구하기
def myprint(q):
    while q != 0:
        q = q - 1
        print(" %d"  % (T[q]), end= "")
    print()

def PI(n, r, q):
    if r == 0:
        myprint(q)
    else:
        for i in range(n-1, -1, -1):



# 중복순열 구하기
# def myprint(q):
#     while q != 0:
#         q = q - 1
#         print(" %d"  % (T[q]), end= "")
#     print()
#
# def PI(n, r, q):
#     if r == 0:
#         myprint(q)
#     else:
#         for i in range(n-1, -1, -1):
#             A[i], A[n-1] = A[n-1] , A[i]
#             T[r-1] = A[n-1]
#             PI(n, r-1, q)
#             A[i], A[n-1] = A[n-1], A[i]
A = [1, 2, 3]
T = [0] * 3
print(PI(3, 2, 2))


# 조합
def comb(n, r):
    memo = [[0] for _ in range(n+1) for _ in range(n+1)]
    for i in range