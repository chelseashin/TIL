import sys
sys.stdin = open("02.txt", "r")

def perm(n, k, sum):
    global ans, data
    if sum > ans:
        return

    if n == k:
        sum += data[Z[k-1]][Z[k]]
        if ans > sum:
            ans = sum

    for i in range(k, n):
        Z[k], Z[i] = Z[i], Z[k]
        perm(n, k+1, sum+data[Z[k-1]][Z[k]])
        Z[k], Z[i] = Z[i], Z[k]

T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)
    ans = 987654321
    Z = [i for i in range(N)] + [0]
    perm(N, 1, 0)
    print("#{} {}".format(tc+1, ans))