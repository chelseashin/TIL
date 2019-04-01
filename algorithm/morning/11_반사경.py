import sys
sys.stdin = open("반사경.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visit = [[0]* N for _ in range(N)]   # 디버깅용
    ans = 0
    dir = 0
    dx = [0, 1, 0, -1]  # 오 아 왼 위
    dy = [1, 0, -1, 0]
    x, y = 0, 0

    while True:
        # visit[x][y] = 1
        x += dx[dir]
        y += dy[dir]

        if x < 0 or x >= N or y < 0 or y >= N:
            break
        if arr[x][y] == 2:
            if dir == 0:
                dir = 1
            elif dir == 1:
                dir = 0
            elif dir == 2:
                dir = 3
            elif dir == 3:
                dir = 2
            ans += 1

        if arr[x][y] == 1:
            if dir == 0:
                dir = 3
            elif dir == 1:
                dir = 2
            elif dir == 2:
                dir = 1
            elif dir == 3:
                dir = 0
            ans += 1
        # 0이 값이면 그냥 계속 감
    print("#{} {}".format(tc+1, ans))
