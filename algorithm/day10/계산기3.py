import sys
sys.stdin = open("계산기3.txt")

T = 10
for tc in range(T):
    N = int(input())
    data = input()
    # data = list(map(str, input().split()))
    print(data)

    op = "+-*/()"
    stack = []
    for i in range(len(data)):
        if data[i] not in op:
            stack.append(int(data[i]))
        elif data[i] == "(" :
            stack.append(data[i])
            if data[i] not in op:
                stack.append(data[i])
            elif data[i] == ")":

        # elif data[i] == "+" or data[i] == "-" or data[i] == "*" or data[i] == "/":
