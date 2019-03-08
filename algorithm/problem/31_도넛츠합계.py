import sys
sys.stdin = open("도넛츠합계.txt")

N, K = map(int, input().split())     # 4, 3
arr = [list(map(int, input().split())) for i in range(N)]
# arr = []
# for i in range(N):
#     arr.append(list(map(int, input().split())))
# print(arr)

def check(x, y):
    left, right, up, down = 0, 0, 0, 0
    for i in range(K):    # 0 1 2
        left += arr[x+i][y]      # 왼
        right += arr[x+i][y+K-1] # 오
        up += arr[x][y+i]        # 위
        down += arr[x+K-1][y+i]  # 아래
        dounuts = left + right + up + down - (arr[x][y] + arr[x][y+K-1] + arr[x+K-1][y] + arr[x+K-1][y+K-1])
    return dounuts


sol = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        dsum = check(i, j)
        if dsum > sol:
            sol = dsum
print(sol)