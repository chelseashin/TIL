N = 10
# N = int(input())

r, c = 0, -1  # 한칸 이전 위치에서 시작
num = 0       # 카운팅할 숫자
cnt = N       # 루프 회전 수
arr = [[0]*N for i in range(N)]

while num < N*N:
    # 오른쪽 방향
    for i in range(cnt):
        c += 1
        num += 1
        arr[r][c] = num
    cnt -= 1

    for i in range(cnt):
        r += 1
        num += 1
        arr[r][c] = num

    for i in range(cnt):
        c -= 1
        num += 1
        arr[r][c] = num
    cnt -= 1

    for i in range(cnt):
        r -= 1
        num += 1
        arr[r][c] = num


for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()



# 달팽이 간단하게 풀기
# n = int(input())
# arr = [[0 for _ in range(n)] for _ in range(n)]
# x, y, i, j = 0, -1, 0, 0
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
#
# for i in range(1, n**2+1):
#     x += dx[j]
#     y += dy[j]
#     arr[x][y] = i
#     if i == n or i == 2*n-1 or i == 3*n-2 or arr[x+dx[j]][y+dy[j]] != 0:
#         if j == 3: j = 0
#         else: j += 1
# for line in arr:
#     print(*line)