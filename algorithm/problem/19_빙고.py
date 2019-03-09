import sys
sys.stdin = open("빙고.txt")

# 빙고 배열
bingo = [list(map(int, input().split())) for _ in range(5)]
# 부르는 숫자 배열
call = [list(map(int, input().split())) for _ in range(5)]

def find(number):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number:
                bingo[i][j] = 0
                return

def Bingo():
    count = 0
    acsum, bcsum = 0, 0
    for i in range(5):
        rsum, csum = 0, 0
        for j in range(5):
            rsum += bingo[i][j]    # 가로의 합
            csum += bingo[j][i]    # 세로의 합
        if rsum == 0:  # 한 행의 합이 0이면 1 빙고
            count += 1
        if csum == 0:
            count += 1
        acsum += bingo[i][i]     # 대각선
        bcsum += bingo[i][5-1-i]
    if acsum == 0:
        count += 1
    if bcsum == 0:
        count += 1

    if count >= 3:   # 빙고가 3개 이상이니?
        return True

    else:
        return False

flag = 0
for i in range(5):
    for j in range(5):
        find(call[i][j])  # 해당 숫자 찾아 지우기
        if Bingo() == True:    # 빙고이면
            flag = 1
            break
    if flag == 1:
        break

# 빙고를 외칠 때의 call 좌표
print(i*5 + j+1)  # 사회자가 부른 횟수