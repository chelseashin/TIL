import sys
sys.stdin = open("색종이배치.txt")

# 나의 풀이
# 행좌표, 열좌표, 가로크기, 세로크기
# R1, C1, G1, S1 = map(int, input().split())   # 2 3 4 4
# R2, C2, G2, S2 = map(int, input().split())   # 6 7 4 4
#
# map = [[0]*101 for i in range(101)]  # 100 * 100 배열
#
#
# # 1번 색종이 붙이기
# for i in range(G1):
#     for j in range(S1):
#         map[R1+i][C1+j] += 1
#
# # 2번 색종이 붙이기
# for i in range(G2):
#     for j in range(S2):
#         map[R2+i][C2+j] += 1
# print(map)
# print(what_type(map))


# 다른 풀이
# r, c, w, h = map(int, input().split())
# arr = [[0]*100 for i in range(100)] # 도화지
#
# # 첫번째 색종이
# for i in range(r-1, r+h+1):
#     for j in range(c-1, c+w+1):
#         if i==r-1 or i == r+h or j==c+w: # 가장자리이면 2로 마킹
#             arr[i][j] = 2
#         else:   # 색종이이면 1로 마킹
#             arr[i][j] = 1
#
# for i in range(20):
#     for j in range(20):
#         print(arr[i][j], end=" ")
#     print()
#
# # 두번째 색종이 - 굳이 찍어볼 필요 없음..
# r, c, w, h = map(int, input().split())

# idea!
# 두번째 색종이의 범위 이내의 1의 개수와 2의 개수 카운팅하기
# type1은 1의 개수 0개이고 2의 개수 1개
# type2는 1의 개수 0개이고 2의 개수 2개 이상
# type3은 1의 개수 1개 이상이면
# 그 외는 type4

sr, sc, w, h = map(int, input().split())
arr = [[0] * 100 for i in range(100)]

for i in range(sr - 1, sr + h + 1):
    for j in range(sc - 1, sc + w + 1):
        if i == sr - 1 or i == sr + h or j == sc - 1 or j == sc + w:
            arr[i][j] = 2
        else:
            arr[i][j] = 1

sr, sc, w, h = map(int, input().split())
cnt1 = 0
cnt2 = 0
for i in range(sr, sr + h):
    for j in range(sc, sc + w):
        if arr[i][j] == 1:
            cnt1 += 1
        elif arr[i][j] == 2:
            cnt2 += 1

if cnt1 == 0 and cnt2 == 1:
    sol = 1
elif cnt1 == 0 and cnt2 > 1:
    sol = 2
elif cnt1 > 0:
    sol = 3
else:
    sol = 4

print(sol)