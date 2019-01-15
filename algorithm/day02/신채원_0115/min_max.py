import sys
sys.stdin = open("min_max.txt")

T = int(input())
# 여러 개의 testcase가 주어지므로 각각을 처리함
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)
    ans = max(data) - min(data)

    print("#{} {}".format(tc + 1, ans))