import sys
sys.stdin = open("오셀로게임.txt")

def iswall(row, col):
    if row < 0 or row >= n or col < 0 or col >= n:
        return True


def find(r, c, stone):
    if stone == 1:
        stone2 = 2
    else:
        stone2 = 1
    board[r][c] = stone
    for pr, pc in deg:
        new_r, new_c = r + pr, c + pc
        # print(new_r, new_c)
        flag = False
        if not iswall(new_r, new_c) and board[new_r][new_c] == stone2:
            while True:
                if not iswall(new_r, new_c):
                    if board[new_r][new_c] == 0:
                        break
                    elif board[new_r][new_c] == stone:
                        flag = True
                        break
                    new_r += pr
                    new_c += pc
                else:
                    break

            if flag:
                new_r, new_c = r + pr, c + pc
                while True:
                    # for i in board:
                    #     print(i)
                    # print()
                    if not iswall(new_r, new_c):
                        if board[new_r][new_c] == stone:
                            break
                        board[new_r][new_c] = stone
                        new_r += pr
                        new_c += pc
                    else:
                        break
    return


deg = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
for tc in range(int(input())):
    n, m = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    board[n // 2][n // 2] = 2

    for i in range(m):
        col, row, stone = map(int, input().split())
        row, col = row - 1, col - 1
        find(row, col, stone)

    black, white = 0, 0
    for i in board:
        for j in i:
            if j == 1:
                black += 1
            elif j == 2:
                white += 1

    print("#{} {} {}".format(tc + 1, black, white))



# 다른 풀이 2

T = int(input())
for test_case in range(T):
    N, P = map(int, input().split())
    data = [[0 for _ in range(N+1)] for _ in range(N+1)]
    data[N // 2 + 1][N // 2], data[N // 2][N // 2 + 1] = 1, 1
    data[N // 2][N // 2], data[N // 2 + 1][N // 2 + 1] = 2, 2 # 오델로 중앙에 W, B 놓기
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]  # 상 하 좌 우 좌상 좌하 우상 우하
    for _ in range(P):
        x, y, P = map(int, input().split())
        data[x][y] = P  # 오델로 데이터 받아오기
        for i in range(8):
            new_x = x + dx[i]   # 돌 바꿔주기 위한작업
            new_y = y + dy[i]
            stack = []
            while 0 < new_x <= N and 0 < new_y <= N:
                if data[new_x][new_y] == 0:
                    break
                elif data[new_x][new_y] != P:
                    stack.append(new_x)
                    stack.append(new_y)
                elif data[new_x][new_y] == P:
                    while stack:
                        turn_y = stack.pop()
                        turn_x = stack.pop()
                        data[turn_x][turn_y] = P
                    break
                new_x += dx[i]
                new_y += dy[i]
    B = 0
    W = 0
    for x in range(N+1):
        for y in range(N+1):
            if data[x][y] == 1:
                B += 1
            elif data[x][y] == 2:
                W += 1
    print("#{} {} {}".format(test_case+1, B, W))