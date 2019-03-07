import sys
sys.stdin = open("반나누기.txt")

T = int(input())
for tc in range(T):
    N, Kmin, Kmax = map(int, input().split())
    score = sorted(list(map(int, input().split())))    # 오름차순으로 정렬된 어학점수 리스트

    div_class = []
    for T1 in range(1, 101):
        for T2 in range(T1+1, 101):
            A = []
            B = []
            C = []
            for i in score:
                if i >= T2:
                    A.append(i)
                elif i < T1:
                    C.append(i)
                else:
                    B.append(i)

            num = [len(A), len(B), len(C)]

            if max(num) <= Kmax and min(num) >= Kmin:
                ans = max(num) - min(num)
                div_class.append(ans)
    if div_class:
        print(min(div_class))
    else:
        print(-1)