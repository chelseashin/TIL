import sys
sys.stdin = open("숫자카드.txt")

T = int(input())
for tc in range(T):      # testcase
    N = int(input())
    data = input()       # 데이터를 int 그대로 받아줌
    # print(data)
    new = [0] * 10
    for i in range(len(data)):
        # print(data[i])
        new[int(data[i])] += 1
    # print(new)

    card = 0
    num = 0
    for i in range(len(new)):
        if new[i] >= num:
            num = new[i]
            card = i

    print("#{} {} {}".format(tc + 1, card, num))