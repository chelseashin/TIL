import sys
sys.stdin = open("미로1.txt")

def isWall(x, y):
    global N, maze
    if arr[x][y] == 1: return True    # 벽이면
    if arr[x][y] == 9: return True
    return False    # 벽이 아님

def maze_dfs(x, y):
    global arr, flag
    dx = [1, -1, 0, 0]    # 상하좌우 검색좌표
    dy = [0, 0, 1, -1]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if arr[new_x][new_y] == 3:    # 목적지에 도달하면
            flag = 1
            break
        if isWall(new_x, new_y) == False:    # 벽이 아니면
            arr[new_x][new_y] = 9     # 9로 바꾸며 나아가기
            maze_dfs(new_x, new_y)
    return flag

T = 10
N = 16
for tc in range(T):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    flag = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                maze_dfs(i, j)

    print("#{} {}".format(tc+1, flag))