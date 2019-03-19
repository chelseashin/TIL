import sys
sys.stdin = open("미로2.txt")

def maze_bfs(x, y):
    global maze, N, flag
    Q = []
    visit[x][y] = 1
    Q.append((x, y))    # 갈 수 있는 곳을 큐에 넣기, 넣고 시작하기

    while len(Q) != 0:    # 큐가 비어있지 않은 동안
        x, y = Q.pop(0)
        for i in range(4):
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            nx = x + dx[i]
            ny = y + dy[i]
            # if isWall(nx, ny) == False:    # 필요 없음.. 0일 때 그냥 무조건 가기 때문에
            if maze[nx][ny] == 3:
                flag = 1
                return
            if maze[nx][ny] == 0 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                Q.append((nx, ny))
    return 0

T = 10
N = 100
for tc in range(T):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # maze = [[int(x) for x in input()] for _ in range(N)]
    visit = [[0] * 100 for _ in range(N)]

    flag = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                maze_bfs(i, j)

    print("#{} {}".format(tc+1, flag))