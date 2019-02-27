import sys
sys.stdin = open("행렬.txt")


def find_first(data):
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j] != 0:
                    return i, j

def find_matrix(x, y):   # 행렬 시작 좌표
    global data
    r = 0  # 행
    c = 0  # 열
    while data[x][y]:
        c += 1
        data[x][y] = 0 # 카운트 한 것은 0으로 바꾸기
        if data[x+1][y] != 0:
            while data[x+i][y+c]:
                r += 1
                data[i][j] = 0
                return r, c

T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)
    # print(len(data))



# 다른 풀이
