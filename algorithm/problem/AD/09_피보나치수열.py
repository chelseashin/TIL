# 자연수 N을 입력 받아 N번째 피보나치 수를 출력하는 프로그램을 작성하여라.
N = 7

# 재귀 1 - time error
# N = int(input())

# def fibo(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# print(fibo(N))

# 재귀 2
def fibo2(n):
    f = [0, 1]
    for i in range(2, n + 1) :
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibo2(N))