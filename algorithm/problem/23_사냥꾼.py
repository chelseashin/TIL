import sys
sys.stdin = open("사냥꾼.txt")

N = int(input())
# map = [list(map(int, input())) for i in range(N)]
san = [[0] * (N+2) for i in range(N+2)]     # 주위를 돌(0)로 둘러싼 산 만들기
for i in range(1, N+1):
    san[i] = [0] + list(map(int, input())) + [0]
# print(san)

# 8방향 델타검색으로 몇 마리 토끼를 잡는지
def catch_rabbit(x, y):
    # 상 하 좌 우, 대각선 4방향
    dx = [-1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, 1, 1, -1, -1]
    count = 0
    for d in range(8):
        for dis in range(1, N):
            if san[x+dx[d]*dis][y+dy[d]*dis] == 0 or san[x+dx[d]*dis][y+dy[d]*dis] == 1:
                break
            elif san[x+dx[d]*dis][y+dy[d]*dis] == 2:
                san[x + dx[d] * dis][y + dy[d] * dis] = 9
                count += 1
    return count


rabbits = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if san[i][j] == 1:
            rabbits += catch_rabbit(i, j)

print(rabbits)