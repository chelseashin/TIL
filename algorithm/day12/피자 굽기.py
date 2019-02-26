import sys
sys.stdin = open("피자 굽기.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    # print(C)

    # idx, C
    new = []
    for i in range(M):
        new.append([i, C[i]])
    # print(new)

    # queue 채우기
    queue = []
    for i in range(N):
        queue.append(new[i])
    # print(queue)

    idx = N
    while queue:
        t = queue.pop(0)
        if t[1] // 2 != 0:  # 치즈 남았으면
            t[1] = t[1] // 2
            queue.append(t)

        elif idx < M:    # 피자의 개수보다 인덱스가 작으면
            queue.append(new[idx])
            idx += 1

    print(f"#{tc+1} {t[0]+1}")