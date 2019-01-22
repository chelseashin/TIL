import sys
sys.stdin= open("금속막대.txt")

T = int(input())
for tc in range(T):      # testcase
    N = int(input())
    data = list(map(int, input().split()))
    # data = input()
    # print(data)
    # print(len(data))   # N * 2
    # first = data[0]

    new = [] # 첫 값 들어있는 쌍의 리스트
    first = 0
    for idx, value in enumerate(data):
        if idx % 2 == 0 and data.count(value)%2 == 1:
            first = idx
    new.append(data[first])
    new.append(data[first+1])
    # print(new)

    i = 0
    while i < len(data):
        if data[first+1] == data[i]:
            first = i
            new.append(data[first])
            new.append(data[first+1])
            i = 0
        else:
            i += 2

    print(f"#{tc + 1}", end=" ")
    for i in range(len(new)):
        print(new[i], end = ' ')
    print()



