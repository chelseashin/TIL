# 나의 풀이
import sys
sys.stdin = open("미로.txt")

def isWall(x, y):
    global N, maze
    if x < 0 or x >= N : return True  # 벽이면
    if y < 0 or y >= N : return True
    if maze[x][y] == 1: return True
    return False    # 벽이 아님

    # isWall함수 - 위 코드와 동일
    # if x >= 0 and x < (N) and y >= 0 and y < (N) and maze[x][y] != 1:
    #     return False
    # if x >= 0 and x < (N) and y >= 0 and y < (N) and maze[x][y] == 3:
    #     return False
    # return True

def sol_maze(x, y):
    global maze, flag
    # 상 하 좌 우 탐색
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        new_x = x + dx[i]   # i가 반복되면서 상/하/좌/우를 적용했을 때의 새로운 좌표 생성
        new_y = y + dy[i]
        if isWall(new_x, new_y) == False:   # 벽이 아닐 경우 아래 코드 시행
            if maze[new_x][new_y] == 3:   # 바닥의 값이 3인 경우 flag 변경하고 출력
                flag = 1
                return flag
            maze[new_x][new_y] = 1   # 바닥의 값이 0인 경우 바닥을 1로 바꾸기
            sol_maze(new_x, new_y)   # 재귀함수를 사용해 앞으로 나아갈 수 있다면 계속 나아갈 것
    return flag


T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    start_x = 0  # 시작할 장소의 x, y좌표
    start_y = 0

    for j in range(len(maze[0])):  # j는 2차원 배열의 x축(가로행에 해당하는 숫자)
        for i in range(len(maze)):  # i는 2차원 배열의 y축(세로열에 해당하는 숫자)
            if maze[i][j] == 2:  # 열 방향 순환
                start_x = i  # 좌표로는 x축에 해당(i=x)
                start_y = j  # 좌표로는 y축에 해당(j=y)

    maze[start_y][start_x] = 1

    flag = 0

    print('#{} {}'.format(tc+1, sol_maze(start_x, start_y)))

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