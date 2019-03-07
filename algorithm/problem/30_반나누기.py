import sys
sys.stdin = open("반나누기.txt")

def check(s, e):
    cnt = 0
    for i in range(s, e+1):
        cnt += arr[i]
    if Kmin <= cnt <= Kmax:
        return cnt
    else:
        return 0

T = int(input())
for tc in range(T):
    N, Kmin, Kmax = map(int, input().split())
    score = sorted(list(map(int, input().split())))    # 오름차순으로 정렬된 어학점수 리스트
    arr = [0] * 101
    for s in score:
        arr[s] += 1

    sol = 100
    cnt = [0] * 3
    for i in range(1, N-1):
        for j in range(i+1, N):
            cnt[0] = check(1, i)
            cnt[1] = check(i+1, j)
            cnt[2] = check(j+1, N)
            if cnt[0] * cnt[1] * cnt[2] == 0:    # '셋 중에 하나라도 0이면' 이라는 뜻
                continue
                temp = max(cnt) - min(cnt)
    if sol == 100:
        print(-1)
    else:
        print(sol)

            # A = sum(score[:i+1])    # 각 반의 인원 수
            # B = sum(score[i+1:j+1])
            # C = sum(score[j+1:])
            # if A >= Kmin and B >= Kmin and C >= Kmin and A <= Kmax and B <= Kmax and C <= Kmax:


    # A = []
    # B = []
    # C = []
    # min_sawon = 0
    # for i in range(N-2):
    #     for j in range(i+1, N-1):    # T1 < T2
    #         T1 = score[i]
    #         T2 = score[j]
    #         for k in range(N):
    #             if score[k] >= T2:
    #                 A.append(score[k])
    #             elif score[k] >= T1 and score[k] < T2:
    #                 B.append(score[k])
    #             elif score[k] < T1:
    #                 C.append(score[k])
    # print(C, B, A)
    # if len(A) >= Kmin and len(B) >= Kmin and len(C) >= Kmin and len(A) <= Kmax and len(B) <= Kmax and len(C) <= Kmax:
    #     min_sawon = min(len(A), len(B), len(C))
    # else:
    #     min_sawon = -1
    # print(min_sawon)

