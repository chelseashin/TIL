import sys
sys.stdin = open("자리배정.txt")
# C 7, R 6
C, R = map(int, input().split())
K = int(input())     # 어떤 관객의 대기번호
seat = [[0]*C for _ in range(R)]  # 공연장

r, c = R, 0    # 시작 좌표
num = 0
count_C = C      # C의 루프 수
count_R = R      # R의 루프 수

if K <= C*R:
    while num < C*R:
        # 위쪽
        for i in range(count_R):
            r -= 1
            num += 1
            seat[r][c] = num
            if seat[r][c] == K:
                print('{} {}'.format(c + 1, R - r))
        count_C -= 1
        # 오른쪽
        for i in range(count_C):
            c += 1
            num += 1
            seat[r][c] = num
            if seat[r][c] == K:
                print('{} {}'.format(c + 1, R - r))
        count_R -= 1
        # 아래쪽
        for i in range(count_R):
            r += 1
            num += 1
            seat[r][c] = num
            if seat[r][c] == K:
                print('{} {}'.format(c + 1, R - r))
        count_C -= 1
        # 왼쪽
        for i in range(count_C):
            c -= 1
            num += 1
            seat[r][c] = num
            if seat[r][c] == K:
                print('{} {}'.format(c + 1, R - r))
        count_R -= 1
else:
    print('0')
# print(seat)

# for i in range(R):
#     for j in range(C):
#         if hall[i][j] == K:
#             print(i+C-1, j+1)