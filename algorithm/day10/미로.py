# 나의 풀이
import sys
sys.stdin = open("미로.txt")

def isWall(x, y):
    global N, maze
    if x < 0 or x >= N : return True  # 벽이면
    if y < 0 or y >= N : return True
    if maze[x][y] != 1: return True
    return False    # 벽이 아님

# def answer(x, y):
#    global maze
#    if maze[x][y] == 3:
#        return 1

def sol_maze(x, y):
    # 상 하 좌 우 탐색
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    global maze, flag
    if maze[x][y] == 2:  # 값이 2일 때 시작
        for i in range(4):
            testX = x + dx[i]    # x값
            testY = y + dy[i]    # y값
            if isWall(testX, testY) == False:
                if maze[testX][testY] == 3:
                    flag = 1
                maze[testX][testY] = 1
                sol_maze(testX, testY)


T = int(input())
for tc in range(T):
    N = int(input())
    # arr = [[0 for _ in range(N)] for _ in range(N)]
    # for i in range(N):
    #     arr[i] = list(map(int, input().split()))
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)
    start = ()
    flag = 0
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                start = (i, j)
    x, y = start[0], start[1]

    sol_maze(x, y)
    print(f"#{tc+1} {flag}")


# 다른 풀이
# def iswall(x,y):
#    global maze, N
#    if x >= 0 and x < (N) and y >= 0 and y < (N) and maze[x][y] != 1:
#        return True
#    if x >= 0 and x < (N) and y >= 0 and y < (N) and maze[x][y] == 3:
#        return True
#    return False
#
# # def answer(x, y):
# #    global maze
# #    if maze[x][y] == 3:
# #        return 1
#
# def move(x,y):
#    global maze, ans
#    dx = [0, 0, -1, 1]
#    dy = [-1, 1, 0, 0]
#
#    for i in range(4):
#        nx = x+dx[i]
#        ny = y+dy[i]
#
#        if iswall(nx, ny):
#            if maze[nx][ny] == 3:
#                ans = 1
#            maze[nx][ny] = 1
#            move(nx, ny)
#
#
# T = int(input())
# for tc in range(T):
#    N = int(input())
#    maze = [list(map(int, input())) for _ in range(N)]
#    start = ()
#    ans = 0
#    for i in range(len(maze)):
#        for j in range(len(maze)):
#            if maze[i][j] == 2:
#                start = (i, j)
#    x, y = start[0], start[1]
#
#    move(x, y)
#    print(f'#{tc+1} {ans}')