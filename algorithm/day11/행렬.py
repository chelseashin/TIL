import sys
sys.stdin = open("행렬.txt")

def find_matrix(x, y):   # 행렬 시작 좌표
    global data
    r = 0  # 행
    c = 0  # 열
    while data[x][y]:
        c += 1
        data[i][j] = 0 # 카운트 한 것은 0으로 바꾸기
        if data[i+1][j] != 0:
            while c == True:
                r += 1
                data[i][j] = 0
    return r, c



T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)
    # print(len(data))

for i in range(len(data)):
    r = 0  # 행
    c = 0  # 열
    for j in range(len(data)):
        if data[i][j] != 0:
            c += 1
            data[i][j] = 0
            if data[i+1][j] != 0:
                r += 1
                while c = True:
                    data[i+1]