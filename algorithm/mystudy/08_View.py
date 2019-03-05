import sys
sys.stdin = open("View.txt", "r")

T = 10
for tc in range(T):
    N = int(input())
    building = list(map(int, input().split()))
    # 나의 풀이
    # view = 0
    # for i in range(2, len(building)):
    #     if building[i] > building[i-1] and building[i] > building[i-2] and building[i] > building[i+1] and building[i] > building[i+2]:
    #         view += building[i]-max(building[i-2], building[i-1], building[i+1], building[i+2])
    #
    # print("#{} {}".format(tc+1, view))



    # 다른 풀이 - for문 2개 활용
    ans = 0
    for i in range(2, len(building)-2):
        min = 987654321
        for j in range(5):
            if j != 2:
                if min > building[i]-building[i-j+2]:
                    min = building[i] - building[i-j+2]
        if min > 0:
            ans += min

    print("#{} {}".format(tc + 1, ans))