import sys
sys.stdin = open("원안의마을.txt")

import math
N = int(input())
land = [list(map(int, input())) for _ in range(N)]

def bangyeong(x, y):   # 최대 반경
    dis = 0    # 기지국까지의 거리
    max_dis = 0    # 최대거리
    for i in range(N):
        for j in range(N):
            if land[i][j] == 1:
                dis = ((x-i)**2 + (y-j)**2) ** (1/2)
            if max_dis < dis:
                max_dis = dis
    return max_dis

for i in range(N):
    for j in range(N):
        if land[i][j] == 2:
            print(math.ceil(bangyeong(i, j)))