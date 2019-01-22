import sys
sys.stdin = open("색칠하기.txt")

T = int(input())
for tc in range(T):
    N = int(input()) # 줄 수
    arr = [[0 for _ in range(10)] for _ in range(10)]
    count = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # print(r1, c1, r2, c2, color)
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color
                # print(arr)
                if arr[i][j] == 3:
                    count += 1
    print(f'#{tc + 1} {count}')