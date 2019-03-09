import sys
sys.stdin = open("배열정리.txt")

# 나의 풀이
X, Y = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(X)]

for i in range(X):
    for j in range(Y):
        if data[i][j] == 1:
            for k in range(1, Y-j):
                if data[i][j+k] == 1:
                    data[i][j+k] = data[i][j+k-1] + 1
                else:
                    break
for i in range(X):
    for j in range(Y):
        print(data[i][j], end=" ")
    print()

# 좋은풀이

# X, Y = map(int, input().split())
# # data = [list(map(int, input().split())) for _ in range(X)]
# # 데이터 받는 다른 방법
# data = []
# for i in range(X):
#     data.append(list(map(int, input().split())))
#
# for i in range(X):
#     for j in range(1, Y):
#         if data[i][j] == 1:
#             data[i][j] += data[i][j-1]
#
# for i in range(X):
#     for j in range(Y):
#         print(data[i][j], end=" ")