import sys
sys.stdin = open("Forth.txt")

T = int(input())
for tc in range(T):
    data = list(map(str, input().split()))
    # print(data)
    # print(len(data))    # 8 5 16

    op = "+-*/."
    stack = []
    for i in range(len(data)):
        if data[i] not in op:
            stack.append(int(data[i]))
        elif data[i] == "+" or data[i] == "-" or data[i] == "*" or data[i] == "/":
            if len(stack) < 2:
                result = "error"
                break

            else:
                num1 = stack.pop()   # 더 늦게 들어온 수 stack[-1]
                num2 = stack.pop()   # stack[-2]
                if data[i] == "+":
                    stack.append(num1 + num2)

                elif data[i] == "-":
                    stack.append(num2 - num1)

                elif data[i] == "*":
                    stack.append(num1 * num2)

                elif data[i] == "/":
                    stack.append(num2 // num1)
        elif data[i] == ".":
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = "error"
                break

    print(f"#{tc+1} {result}")