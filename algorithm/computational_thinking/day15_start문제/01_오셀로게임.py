import sys
sys.stdin = open("오셀로게임.txt")

def iswall(x, y):
    if 0 < x <= N and 0 < y <= N:False     # 벽이 아님
    else: True     # 벽임

# 오셀로 게임 실행 - 재귀로 풀어보자
def osello(x, y):
    global game, M
    game[x][y] = dol    # 주어진 위치에 돌 놓기
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [-1, 0, 1, -1, 0, 1, 1, -1]
    for i in range(8):
        new_x = x + dx[i]    # 돌 바꿔주기
        new_y = y + dy[i]

    stack = []
    while iswall == False:
        if game[new_x][new_y] == 0:
            break
        elif game[new_x][new_y] != dol:    # 같지 않으면
            stack.append(new_x, new_y)
        elif game[new_x][new_y] == dol:    # 같은 돌이면
            while stack == True:
                diff_y = stack.pop()
                diff_x = stack.pop()
                game[diff_x][diff_y] = dol
            break
        new_x += dx[i]
        new_y += dy[i]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # 4, 12
    game = [[0 for _ in range(N)] for _ in range(N)]
    # 게임판 중앙에 검은돌, 흰돌 놓기
    game[N // 2 - 1][N // 2 - 1] = 2
    game[N // 2 - 1][N // 2] = 1
    game[N // 2][N // 2 - 1] = 1
    game[N // 2][N // 2] = 2
    # print(game)
    for play in range(M):    # 12
        x, y, dol = list(map(int, input().split()))
        osello(x, y)      # 오셀로 게임 함수 실행
        # print(game)     # 확인

        white = 0
        black = 0
        for i in range(N):
            for j in range(N):
                if game[i][j] == 1:
                    white += 1
                if game[i][j] == 2:
                    black += 1
    print(black, white)
    # print("#{} {} {}".format(T, black, white))