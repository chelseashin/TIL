import sys
sys.stdin = open("문제1.txt")

T = int(input())
N, K = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(N)]    # 게임판

def sum_left(x, y):     # 왼쪽 대각선 값의 합(\)
    value = 0
    for i in range(K):
        value += game[x+i][y+i]
    return value


def sum_right(x, y):    # 오른쪽 대각선 값의 합(/)
    value = 0
    for i in range(K):
        value += game[x+i][y+K-1-i]
    return value

right = 0  # 오른쪽 대각선 값
left = 0  # 왼쪽 대각선 값
ans = 987654321      #  오른쪽 대각선의 합과 왼쪽 대각선의 합의 차이가 가장 작은 값
for i in range(N-K+1):
    for j in range(N-K+1):
        if game[i][j] >= 0:
            left = sum_left(i, j)
            right = sum_right(i, j)
            diff = max(right, left) - min(right, left)
            if ans > diff:
                ans = diff

print("#{} {}".format(T, ans))