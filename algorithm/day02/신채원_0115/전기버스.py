import sys
sys.stdin = open("전기버스.txt")

T = int(input())
for tc in range(T):      # test case
    # N = int(input())
    ans = 0
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # print(data)
    count = 0
    cp = 0
    current = 0

    while current + K < N:

        for i in range(1, K + 1):
            if current + i in data:
                cp = current + i

        if current == cp:
            count = 0
            break
        count += 1
        current = cp

    print("#{} {}".format(tc + 1, count))