import sys
sys.stdin = open("농작물수확하기.txt")


T = int(input())
for tc in range(T):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    # print(farm)

    # 첫값 찾기
    mid = N//2
    start = mid
    end = mid
    sum = 0
    for i in range(N):
        for j in range(start, end+1, 1):
            sum += farm[i][j]
        if i < mid:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print("#{} {}".format(tc+1, sum))