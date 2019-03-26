def myprint(q):
    while q != 0:
        q = q - 1
        print(" %d " % (T[q]), end="")
    print()

# 중복 허용 X
# def combination(n, r, q):
#     if r == 0:
#         myprint(q)
#     else:
#         if n < r:
#             return
#         else:
#             T[r-1] = A[n-1]
#             combination(n, r-1, q)
#             combination(n-1, r, q)

# 중복을 허용
def combination(n, r, q):
    if r == 0:
        myprint(q)
    elif n == 0:
        return
    else:
        if n < r:
            return
        else:
            T[r-1] = A[n-1]
            combination(n, r-1, q)
            combination(n-1, r, q)

A = [1, 2, 3, 4]
T = [0] * 3
print(combination(4, 3, 3))