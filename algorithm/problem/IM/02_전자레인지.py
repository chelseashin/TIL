# 좋은풀이 - 최소 버튼 횟수
# T = int(input())
T = 100
a, b, c = 300, 60, 10

A = T // a    # 몫
T = T % a     # 나머지

B = T // b
T = T % b

C = T // c
T = T % c

if T == 0:
    print(A, B, C)
else:
    print(-1)