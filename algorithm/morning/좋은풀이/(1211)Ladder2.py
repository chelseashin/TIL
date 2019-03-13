# 프로그램을 짤 때 기능별로 모듈화를 해서 짜보는 연습을 해보자

def check(x, y, visit):
    if x < 0 or x >= SIZE:  return False
    if y < 0 or y >= SIZE:  return False
    if data[x][y] == 0:     return False
    if visit[x][y] == 1:    return False
    return True

def getCnt(x, y):
    dx = [ 0, 0, 1]
    dy = [-1, 1, 0]  #왼쪽, 오른쪽, 아래쪽
    visit = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    cnt = 0
    visit[x][y] = 1

    while (True):                 # 갈 수 있는 길이면 x, y 좌표를 바꿈
        if x == SIZE - 1: break
        for j in range(3):
            nx = x + dx[j]
            ny = y + dy[j]
            if check(nx, ny, visit):
                x = nx
                y = ny
                visit[x][y] = 1    # 방문했던 것을 처리
                cnt += 1
                break
    return cnt

def solve(): # data[x][y]
    min = 0x7fffffff        # 십진수중에 가장 큰 수
    ret = 0
    cnt = 0
    for i in range(SIZE):
        if data[0][i]:
            cnt = getCnt(0, i)
        if cnt < min :
            min = cnt
            ret = i
    return ret

import sys
sys.stdin = open("(1211)Ladder2_input.txt")
T = 10
SIZE = 100
for tc in range(T):
    no = int(input())
    data=[list(map(int, input().split())) for _ in range(SIZE)]
    # visit = [[0 for _ in range(SIZE)]for _ in range(SIZE)]
    print("#{} {}".format(tc+1,solve()))
