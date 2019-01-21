arr = [[0, 1, 2, 3],
       [4, 5, 6, 7],
       [8, 9, 10, 11]]

# print(len(arr))
# print(len(arr[2]))
# # i : 행의 좌표, n = len(arr)
# # j : 열의 좌표, m = len(arr)
#
# # 행 우선
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end = " ")
#     print()
# print()
#
# # 열 우선
# for j in range(len(arr[0])):
#     for i in range(len(arr)):
#         print(arr[i][j], end = " ")
#     print()
# print()
#
# # 지그재그 순회
# n = len(arr)
# m = len(arr)
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         print(arr[i][j + (m-1-2*j) * (i%2)])
#     print()
# print()


# 풀이
def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return False
def calAbs(y, x):
    if y > x:
        return y * x
    else:
        return x * y

###
dx = [0, 0, -1, 1]
dy = [ -1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += calAbs(arr[y][x], arr[testY][testX])
print("sum = {}".format(sum))