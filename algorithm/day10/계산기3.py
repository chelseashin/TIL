import sys
sys.stdin = open("계산기3.txt")

# data = "3+(4+5)*6+7"
T = 10
for tc in range(T):
    N = int(input())
    data = input()
    # data = list(map(str, input().split()))
    # print(data)

stack = []
result = []
for i in range(len(data)):
    if data[i] == "(":
        stack.append(data[i])

    elif data[i].isdigit():
        result.append(data[i])

    elif data[i] == "+":
        if len(stack) == 0:
            stack.append(data[i])
        elif stack[-1] == "(":
            # "(" in stack:
            stack.append(data[i])
        elif stack[-1] == "+":
            # stack.pop()
            result.append(data[i])
        elif stack[-1] == "*":
            result.append(stack.pop())
            if stack[-1] == "+":
                result.append(data[i])


    elif data[i] == "*":
        if len(stack) == 0:
            stack.append(data[i])
        elif "(" in stack or stack[-1] == "+":
            stack.append(data[i])
        elif stack in "*":
            result.append(stack.pop())


    elif data[i] == ")":
        while True:
            result.append(stack.pop())
            if stack[-1] == "(":
                stack.pop()
                break

if len(stack) != 0:
    while True:
        result.append(stack.pop())
        if len(stack) == 0:
            break

print(''.join(result))



#     print(f"#{tc + 1} {result}")




# 수식을 eval() 내장 함수로 계산
# 스택을 두번 사용해서 처리했던 연산을
# 파이썬으로 제공되는 eval() 내장 함수로 계산할 수 있음
# 문자열로 된 수식을 계산함
# 이러면 답이 됨!
#     print(f"#{tc + 1} {eval(data)}")