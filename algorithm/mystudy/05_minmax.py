import sys
sys.stdin = open("min_max.txt", "r")

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    max_num = 0
    min_num = 987654321
    for i in range(len(data)):
        if data[i] > max_num:
            max_num = data[i]
        elif data[i] < min_num:
            min_num = data[i]

    print("#{} {}".format(tc+1, max_num-min_num))