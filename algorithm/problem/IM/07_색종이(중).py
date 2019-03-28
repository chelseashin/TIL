import sys
sys.stdin = open("색종이(중).txt")

N = int(input())

# 예외처리 안하기 위해 배열을 넉넉하게 만드는 것이 포인트!
arr = [[0] * 110 for i in range(110)]
for i in range(N):
    R, C = map(int, input().split())

    # 도화지에서 색종이 붙이기
    for i in range(R, R+10):
        for j in range(C, C+10):
            arr[i][j] = 1

def diff(x, y):
    sol = 0
    # 다 물어봐야 하기 때문에 elif가 아니라 모두 if를 써야 한다!
    if arr[x-1][y] == 0:  # 상
        sol += 1
    if arr[x-1][y] == 0:  # 하
        sol += 1
    if arr[x][y-1] == 0:  # 좌
        sol += 1
    if arr[x][y+1] == 0:  # 우
        sol += 1
    return sol


result = 0
for i in range(110):
    for j in range(110):
        if arr[i][j] == 1:
            # 둘레 구하는 함수
            result += diff(i, j)
print(result)