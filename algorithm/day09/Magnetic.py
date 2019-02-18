import sys
sys.stdin = open("Magnetic.txt")

T = 10
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    # 1 : N극 성질 가지는 자성체(위)
    # 2 : S극 성질 가지는 자성체(아래)

    cnt = 0
    for i in range(N):   # 행
        stack = 0
        for j in range(N):  # 열
            if arr[j][i] == 1:
                stack = 1
            elif arr[j][i] == 2:
                if stack == 1:
                    cnt += 1
                    stack = 0

    print(f"#{tc + 1} {cnt}")