# 부분집합의 합
import sys
sys.stdin = open("부분집합의 합.txt")

T = int(input())
for tc in range(T):      # testcase
    N, K = map(int, input().split())
    # print(data)
    # print(len(data))

    arr = list(range(1, 13))     # len(arr) = 12
    result = 0
    for i in range(1, 1 << len(arr)):      # 1<<n : 부분 집합의 개수
        sum = 0
        cnt = 0
        for j in range(len(arr)):          # 원소의 수만큼 비트를 비교함  range(arr[0])
            if i & (1 << j):               # i의 j번째 비트가 1이면 j번재 원소 출력
                sum += arr[j]
                cnt += 1

        if sum == K and cnt == N:
            result = 1

    print(f"#{tc + 1} {result}")