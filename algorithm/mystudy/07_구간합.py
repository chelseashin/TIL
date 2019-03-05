import sys
sys.stdin = open("구간합.txt", "r")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    max_sum = 0
    min_sum = 987654321
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += data[i+j]
        if max_sum < sum:
            max_sum = sum
        if min_sum > sum:
            min_sum = sum

    print("#{} {}".format(tc+1, max_sum-min_sum))