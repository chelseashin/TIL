import sys
sys.stdin = open("구슬굴리기.txt")

R, C = map(int, input().split())
# 1로 맵 둘러싸기
arr = [[1 for i in range(R+2)] for _ in range(R+2)]
for i in range(1, R+1):
    arr[i] = [1] + list(map(int, input())) + [1]
# print(arr)
N = int(input())
dir = list(map(int, input().split()))   # 2 3 1 4 1 3

def marble(x, y):
    # 방향순서
    can = 0
    # 원래 위치, 위, 아래, 좌, 우
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    # 전체 칸 수
    count = 0

    while True:
        if arr[x][y] == 2:
            arr[x][y] = 0
            can += 1
        elif arr[x+dx[dir[can]]][y+dy[dir[can]]] == 1:
            arr[x + dx[dir[can]]][y + dy[dir[can]]] = 9
            count += 1
            if can > N-1:
                can = 0
        else:
            break
    return count

for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == 2:
            print(marble(i, j))
