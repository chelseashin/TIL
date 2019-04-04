import sys
sys.stdin = open("회문.txt")

def my_rpalindrome(data):
    global flag, M, N
    count = 0
    for i in range(M):    # 행
        for j in range(M-N+1):   # 열
            flag = 1
            for k in range(N//2):   # 주어진 크기만큼
                if data[i][j+k] != data[i][j+N-1-k]:
                    flag = 0
                    break
            if flag:
                count += 1
    return count

def my_cpalindrome(data):
    global flag, M, N
    count = 0
    for i in range(M):
        for j in range(M-N+1):
            flag = 1
            for k in range(N//2):
                if data[j+k][i] != data[j+N-1-k][i]:
                    flag = 0
                    break
            if flag:
                count += 1
    return count


T = 10
for tc in range(T):
    M = 8
    N = int(input())
    # data = [list(map(str,input())) for _ in range(8)]
    data = [input() for _ in range(M)]
    # print(data)
    count = 0

    print("#{} {}".format(tc+1, my_rpalindrome(data) + my_cpalindrome(data)))