# 팩토리얼 함수
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

# 팩토리얼 함수 - 2
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print(fact(5))

# 피보나치 수열 함수 1
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(8))
print(fibo(20))

# 피보나치 2
# 위의 피보나치 수열 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면(memoize),
# 실행시간을 크게 줄일 수 있다.
def fibo1(n):
    # global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
print(fibo1(8))
print(fibo1(20))
print(fibo1(100))


# 피보나치 3 - DP 적용 알고리즘(DP: 점화식)
# 동적 계획(Dynamic Programming) 알고리즘은 최적화 문제를 해결하는 알고리즘.

def fibo2(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibo2(1000))

