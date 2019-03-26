import sys
sys.stdin = open("01.txt", "r")

def iswall(x, y, N):
    if x < 0 or x >= N: return True    # 벽이면
    if y < 0 or y >= N: return True
    return False    # 벽이 아니면

def move(x, y, distance, N):
    global ans
    if distance > ans:
        return

    if x == N - 1 and y == N - 1:
        distance += data[x][y]
        if ans > distance:
            ans = distance
    ex, ey = x, y
    dx = [1, 0]
    dy = [0, 1]
    for i in range(2):
        new_x = ex + dx[i]
        new_y = ey + dy[i]

        if not iswall(new_x, new_y, N):
            move(new_x, new_y, distance + data[ex][ey], N)

T = int(input())

for tc in range(T):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321

    start_x, start_y = 0, 0
    move(start_x, start_y, 0, N)

    print("#{} {}".format(tc+1, ans))
