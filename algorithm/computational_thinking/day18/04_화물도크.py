import sys
sys.stdin = open("04.txt", "r")

T = int(input())
for tc in range(T):
    N = int(input())
    L = []
    for n in range(N):
        s, e = map(int, input().split())
        L.append((s, e))

    L.sort(key=lambda x:x[1])   # 튜플 두번째 요소에 의해 정렬
    # print(L)
    visited = [0 for _ in range(24)]
    cnt = 0
    for i in range(N):
        if 1 in visited[L[i][0]:L[i][1]]:
            pass
        else:
            for i in range(L[i][0], L[i][1]):
                visited[i] = 1
            cnt += 1
    print("#{} {}".format(tc+1, cnt))