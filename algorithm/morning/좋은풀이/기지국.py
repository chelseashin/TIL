import sys
sys.stdin = open("기지국_input.txt","r")

def printArr():
    for i in range(N):
        for j in range(N):
            print(map[i][j], end="")
        print()
    print()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    AnswerN = 0

    map = [list(input()) for _ in range(N)]
    printArr()
    for i in range(N):
        for j in range(N):
            if map[i][j] != 'X' and map[i][j] != 'H': #기지국일 경우
                for k in range(1, ord(map[i][j]) - ord('A') + 2):
                    if i + k < N and map[i + k][j] == 'H':  #남
                        map[i + k][j] = 'X'
                    if j + k < N and map[i][j + k] == 'H':  #동
                        map[i][j + k] = 'X'
                    if i - k > -1 and map[i - k][j] == 'H': #북
                        map[i - k][j] = 'X'
                    if j - k > -1 and map[i][j - k] == 'H': #서
                        map[i][j - k] = 'X'
    printArr()
    for i in range(N):
        for j in range(N):
            if map[i][j] == 'H':
                AnswerN += 1

print("#{0} {1}".format(tc, AnswerN))
