import sys
sys.stdin = open("이진수2.txt")

T = int(input())
for tc in range(T):
    N = float(input())
    # print(N)

    ans = ""
    while N <= float(1):
        N *= 2
        if N > 1:
            ans += '1'
            N -= 1
        elif N < 1:
            ans += '0'

        if N == float(1):
            ans += '1'
            break

    if len(ans) > 12:
        ans = "overflow"

    print("#{} {}".format(tc + 1, ans))