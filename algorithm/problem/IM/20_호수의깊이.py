import sys
sys.stdin = open("호수의깊이.txt")

N = int(input())
lake = [list(map(int, input().split())) for _ in range(N)]

# 호수 깊이 체크
def check_depth(x, y):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for depth in range(1, N):    # depth를 알기 위해!
        for j in range(4):
            if lake[x+dx[j]*depth][y+dy[j]*depth] == 0:
                return depth     # 그 때의 깊이를 리턴

# 호수 깊이 만들기
for i in range(1, N-1):
    for j in range(1, N-1):
        if lake[i][j] == 1:
            ans = check_depth(i, j)
            lake[i][j] = ans
# print(lake)

# 총 깊이 구하기
height = 0
for i in range(N):
    for j in range(N):
        if lake[i][j] != 0:
            height += lake[i][j]
print(height)