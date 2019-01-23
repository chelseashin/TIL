import sys
sys.stdin= open("금속막대.txt")

T = int(input())
for tc in range(T):      # testcase
    N = int(input())
    data = list(map(int, input().split()))
    # data = input()
    # print(data)
    # print(len(data))

    new = []
    first = data[0]
    for idx, value in enumerate(data):
        # print(idx, value)
        if idx % 2 == 0 and data[idx+1] == data.count(value)%2 == 1:
            first = idx
    new.append(data[first])
    new.append(data[first+1])

    i = 0
    for i in len(data):
        if data[]


    # print(f"{tc + 1} {}")