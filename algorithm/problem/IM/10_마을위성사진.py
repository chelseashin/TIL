import sys
sys.stdin = open("마을위성사진.txt")

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

# def how_many(x, y):
#     sol = 0
#     # 다 물어봐야 하기 때문에 elif가 아니라 모두 if를 써야 한다!
#     if arr[x-1][y] == 1:  # 상
#         sol += 1
#     if arr[x-1][y] == 1:  # 하
#         sol += 1
#     if arr[x][y-1] == 1:  # 좌
#         sol += 1
#     if arr[x][y+1] == 1:  # 우
#         sol += 1
#     return sol
#
# highest = 0
# me = 1
# for i in range(N):
#     flag = 0
#     for j in range(1, N):
#         if arr[i][j] == me:
#             if how_many(i, j) == 4:
#                 arr[i][j] += 1

# 큰 루프. 배열의 높이만큼 돌기

for h in range(1, N):
    flag = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] >= h:
                flag = 1
                # 상하좌우 검사
                if arr[i-1][j] > h and arr[i+1][j] > h and arr[i][j-1] > h and arr[i][j+1] > h:
                    arr[i][j] += 1
    if flag == 0:
        break
print(arr)