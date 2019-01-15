import sys
sys.stdin = open("구간합.txt")

T = int(input())
for tc in range(T):      # test case
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # print(data)
    max = 0
    min = 987654321
    for i in range(N-M+1):
        sum = 0
        for j in range(i, i+M):
            sum += data[j]
        if sum > max:
            max = sum
        if sum  < min:
            min = sum
    print("#{} {}".format(tc + 1, max - min))