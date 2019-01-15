import sys
sys.stdin = open("전기버스.txt")

T = int(input())
for tc in range(T):      # test case
    # N = int(input())
    ans = 0
    data = list(map(int, input().split()))
    print(data)



    # print("#{} {}".format(tc + 1, ans))