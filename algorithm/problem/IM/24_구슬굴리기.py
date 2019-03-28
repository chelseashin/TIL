import sys
sys.stdin = open("구슬굴리기.txt")

R, C = map(int, input().split())
# 1로 맵 둘러싸기
arr = [[1 for i in range(C+2)] for _ in range(R+2)]
for i in range(1, R+1):
    arr[i] = [1] + list(map(int, input())) + [1]
# print(arr)
N = int(input())
dir = list(map(int, input().split()))   # 2 3 1 4 1 3

# 좌표 받으면 움직이면서 몇칸 움직였는지 체크
def marble(x, y):
    # 방향순서
    dno = 0
    # 원래 위치, 위, 아래, 좌, 우
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    # 전체 칸 수
    distance = 1

    while dno < N:
        x += dx[dir[dno]]
        y += dy[dir[dno]]

        if arr[x][y] == 0:
            arr[x][y] = 9
            distance += 1

        elif arr[x][y] == 1:  # 벽이면 전단계로 이동하고 방향 전환
            x = x-dx[dir[dno]]
            y = y-dy[dir[dno]]
            dno += 1
            continue
    return distance

for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == 2:
            arr[i][j] = 9
            print(marble(i, j))    # 구슬이 지나간 칸 수