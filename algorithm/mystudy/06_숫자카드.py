import sys
sys.stdin = open("숫자카드.txt", "r")

T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(map(int, input()))
    # cards = input()

    new = [0] * 10
    for i in range(len(cards)):
        new[cards[i]] += 1
    # print(new)

    card = 0
    num = 0
    for i in range(len(new)):
        if new[i] >= num:
            num = new[i]
            card = i
    print("#{} {} {}".format(tc+1, card, num))