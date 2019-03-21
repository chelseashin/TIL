import sys
sys.stdin = open("어디에단어.txt")

T = int(input())
maxN = 15
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    
    visit = [[0] * N for _ in range(N)]    # 가로 체크
    ans = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0 or visit[i][j] == 1: continue
            cnt = 0
            k = j
            while k < N and data[i][k] == 1:
                visit[i][k] = 1
                cnt += 1
                k += 1
            if cnt == K: ans += 1
            
    visit = [[0] * N for _ in range(N)]    # 세로 체크
    for i in range(N):
        for j in range(N):
            if data[j][i] == 0 or visit[j][i] == 1: continue
            cnt = 0
            k = j
            while k < N and data[k][i] == 1:
                visit[k][i] = 1
                cnt += 1
                k += 1
            if cnt == K: ans += 1

    print("#{} {}".format(tc, ans))