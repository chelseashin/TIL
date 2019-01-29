import sys
sys.stdin = open("회문2.txt")

def rmax_pal(data, N, M):
    # 가로 탐색
    while M > 0:
        for i in range(N):
            for j in range(N-M+1):
                flag = 1
                for k in range(M//2):
                    if data[i][j+k] != data[i][j+M-1-k]:
                        flag = 0
                        break
                if flag:
                    return M
        M -= 1

    # 세로 탐색
def cmax_pal(data, N, M):
    while M > 0:
        for i in range(N):
            for j in range(N-M+1):
                flag = 1
                for k in range(M//2):
                    if data[j+k][i] != data[j+M-1-k][i]:
                        flag = 0
                        break
                if flag:
                    return M
        M -= 1

T = 10
for tc in range(T):      # testcase
    no = int(input())
    data = [input() for _ in range(100)]
    # print(data)
    N = len(data)
    # print(N)    # 100
    M = 100

    print(f"#{tc + 1} {max(rmax_pal(data, N, M), cmax_pal(data, N, M))}")