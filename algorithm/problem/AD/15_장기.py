import sys
sys.stdin = open('15.txt')

def mal_bfs(x, y):
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    Q = []
    Q.append((x, y, 0))    # 큐를 만들고 시작 좌표값과 카운트 넣기
    jangi[x][y] = 1        # 시작점 표시

    while Q:    # 큐에 값이 있을 동안
        x, y, cnt = Q.pop(0)
        if x == zx and y == zy:    # 목적지를 만나면
            return cnt             # 카운트 리턴

        for i in range(8):    # 8방향
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:   # 벽이면
                continue
            if jangi[nx][ny] != 1:            # 목적지 만나지 못하면
                Q.append((nx, ny, cnt + 1))   # 큐에 넣고
                jangi[nx][ny] = 1             # 방문 체크

N, M = map(int, input().split())
mx, my, zx, zy = map(int, input().split())
jangi = [[0] * M for _ in range(N)]

mx -= 1; my -= 1; zx -= 1; zy -= 1;
print(mal_bfs(mx, my))    # 시작하는 곳을 넣기