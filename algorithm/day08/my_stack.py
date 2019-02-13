# 괄호 검사
import sys
sys.stdin = open("반복문자 지우기.txt")

T = int(input())
for tc in range(T):
    data = input()
    # print(data)

    stack = []
    for i in range(len(data)):
        if len(stack) == 0:
            stack.append(data[i])
        else:
            if stack[-1] != data[i]:
                stack.append(data[i])
            else:
                stack.pop()

    print(f"#{tc + 1} {len(stack)}")


# 괄호검사
import sys
sys.stdin = open("괄호검사.txt")

T = int(input())
for tc in range(T):
    data = str(input())
    # print(data)

    def make_gwalho(data):
        gwalho = ""
        g = '(){}'
        for i in range(len(data)):
            if data[i] in g:
                gwalho += data[i]
        return gwalho
    # print(make_gwalho(data))

    def check_gwalho(data):
        s = []
        for i in range(len(data)):
            if len(s) == 0:
                s.append(data[i])
            else:
                if s[-1] == '(':
                    if data[i] == ')':
                        s.pop()
                    else:
                        s.append(data[i])
                elif s[-1] == '{':
                    if data[i] == '}':
                        s.pop()
                    else:
                        s.append(data[i])
        if len(s) > 0:
            return 0
        else:
            return 1

    print(f"#{tc + 1} {check_gwalho(make_gwalho(data))}")