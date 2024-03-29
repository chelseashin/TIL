import sys
sys.stdin = open("같은모양찾기.txt")

M = int(input())  # 10
marr = [list(map(int, input())) for _ in range(M)]

# 원본 패턴
P = int(input())  # 3
parr = [list(map(int, input())) for _ in range(P)]

# 90도 회전한 패턴
parr90 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        parr90[j][P-i-1] = parr[i][j]
print(parr90)

# 180도
parr180 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        parr180[P-i-1][P-j-1] = parr[i][j]
print(parr180)

# 270도
parr270 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        parr270[P-j-1][i] = parr[i][j]
print(parr270)

# 합계 구하기
sol = 0
for i in range(M-P+1):
    for j in range(M-P+1):
        if marr[i][j] == parr[0][0]:
            cnt = 0
            for k in range(P):
                for l in range(P):
                    if marr[i+k][j+l] == parr[k][l]:
                        cnt += 1
                    if marr[i+k][j+l] == parr90[k][l]:
                        cnt += 1
                    if marr[i+k][j+l] == parr180[k][l]:
                        cnt += 1
                    if marr[i+k][j+l] == parr270[k][l]:
                        cnt += 1
            if cnt == P*P:    # 9개 모두 매치하면
                sol += 1
print(sol)