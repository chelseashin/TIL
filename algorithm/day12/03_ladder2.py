import sys
sys.stdin = open("ladder2.txt")

def iswall():
    global ladder, x, y
    if ladder[x][y] == 0:
        return True    # 0이면 벽. 벽이면 True
    else:
        return False

def move(x, y):    # 각 시작점에서 도착점 1을 만날 때까지의 여러 거리들 중 최소값을 구하는 함수
    dx = [0, 0, 1]
    dy = [1, -1, 0]
    new_x, new_y = 0, 0
    for i in range(3):
        if isWall == False:
            new_x = x + dx[i]
            new_y = y + dy[i]

    while new_x == 99:
        if isWall() == False:
            start_x += 1
            start_y
        ladder[start_x][start_y]

T = 10
for tc in range(T):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    start_L = []     # 시작점 x좌표들 리스트
    for i in range(100):
        if ladder[0][i] == 1:
            start_L.append(i)

    distance = []    # 시작점별 도착점까지의 최소거리들의 리스트
    for i in start_L:
        start_x = i
        start_y = 0
        distance.append(move(start_x, start_y))
        num = distance.index(min(distance))    # 그 중 가장 짧은 거리가 있는 인덱스
        ans = start_L[num]                     # start_L 에서의 그 인덱스 번호
    print("#{} {}".format(tc+1, ans))