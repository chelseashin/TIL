import sys
sys.stdin = open("미로탈출.txt")

N = int(input())
maze = [[1]*(N+2) for i in range(N+2)]
for i in range(1, N+1):
    maze[i] = [1] + list(map(int, input())) + [1]
dir = list(map(int, input().split()))    # 1 4 3 2

# 인덱스를 제어하라! 인덱스가 어떻게 바뀌고 제어되는지 이유를 계속해서 생각해야 함.

dno = 0    # 방향의 순서
dx = [0, 1, 0, -1, 0]    # 원래 좌표, 아, 왼, 위, 오
dy = [0, 0, -1, 0, 1]
x, y = 1, 1    #
cnt = 0

while True:
    x = x + dx[dir[dno]]
    y = y + dy[dir[dno]]

    if maze[x][y] == 0:  # 0이면 방문표시하고 카운트
        maze[x][y] = 9
        cnt += 1

    elif maze[x][y] == 1:  # 1이면 이전좌표로 이동하고 방향 전환
        x = x - dx[dir[dno]]
        y = y - dy[dir[dno]]
        dno += 1
        if dno > 3:
            dno = 0

    else:    # 지나간 자리이면 탈출
        break
# print(maze)
print(cnt)