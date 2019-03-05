import sys
sys.stdin = open("월동준비.txt")

N = int(input())
dotori = list(map(int, input().split()))
print(dotori)

def stupid(dotori):

    food = dotori[0]
    result = dotori[0]
    for i in range(1, len(dotori)):
        food = max(food + dotori[i], dotori[i])
        result = max(food, result)
    return result

    # for i in range(len(dotori)):
    #     max_taste = 0
    #     for j in range(N-i):
    #         if dotori[i+j] > max_taste:
    #             max_taste += dotori[i+j]
    # return max_taste

def smart(dotori):
    food = 0
    for i in dotori:
        if i >= 0:
            food += i
    return food

print(stupid(dotori), smart(dotori))