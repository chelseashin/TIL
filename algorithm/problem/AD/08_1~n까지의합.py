# 한 정수 n을 입력 받아서 1부터 n까지의 합을 구하여 출력하시오.
# 단, 반드시 재귀함수로 구현하시오.

n = 10
# n = int(input())
def plus(N):
    if N <= 1:
        return 1
    else:
        return N + plus(N-1)

print(plus(n))


# 재귀 X
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)