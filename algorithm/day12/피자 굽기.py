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
<<<<<<< HEAD
    print(new)
=======
    # print(new)
>>>>>>> f889023d21ee06bce0a3af518e88ea3be20c9f17

    # queue 채우기
    queue = []
    for i in range(N):
        queue.append(new[i])
    # print(queue)

    idx = N
    while queue:
<<<<<<< HEAD
        t = queue.pop(0)    # queue의 첫번째 요소를 확인하며 계속해서 뺀다.
=======
        t = queue.pop(0)
>>>>>>> f889023d21ee06bce0a3af518e88ea3be20c9f17
        if t[1] // 2 != 0:  # 치즈 남았으면
            t[1] = t[1] // 2
            queue.append(t)

        elif idx < M:    # 피자의 개수보다 인덱스가 작으면
            queue.append(new[idx])
            idx += 1

<<<<<<< HEAD
    print(f"#{tc+1} {t[0]+1}")
=======
    print(f"#{tc+1} {t[0]+1}")
>>>>>>> f889023d21ee06bce0a3af518e88ea3be20c9f17
