import sys
sys.stdin = open("view_input.txt")       # 표준 입력
T = 10
ans = 0
for tc in range(T):      # testcase
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)
    for i in range(len(data)):
        if data[i] > data[i-1] and data[i] > data[i-2] and data[i] > data[i+1] and data[i] > data[i+2]:
            ans += data[i] - max(data[i-1], data[i-2], data[i+1], data[i+2])
    print("#{} {}".format(tc + 1, ans))
