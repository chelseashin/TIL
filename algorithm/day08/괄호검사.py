import sys
sys.stdin = open("괄호검사.txt")

def make_gwalho(data):
    gwalho = ""
    g = '(){}'
    for i in range(len(data)):
        if data[i] in g:
            gwalho += data[i]
    return gwalho

# 다시 함수 만들어 풀어보자!
# def check_gwalho(data):
#     check = []
#     for i in range(len(data)):
#         if data[i] == '(':
#             check.append(data[i])
#         elif data[i] == ')':
#
#     if len(s) > 0:    # 짝 이루어 s에 값 없으면 1
#         return 0
#     else:             # 짝 이루지 못하면 0
#         return 1

s = []
def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print("Stack is empty!")
        return
    else:
        return s.pop(-1)

# 빈 리스트인지 확인하는 함수
def isEmpty():
    if len(s) == 0:
        return True
    else:
        return False

def check_gwalho(data):
    for i in range(len(data)):
        if data[i] == "(":
            push(data[i])
        elif data[i] == ")":
            if isEmpty():
                return 0
            pop()

        if data[i] == "{":
            push(data[i])
        elif data[i] == "}":
            if isEmpty():
                return 0
            pop()

    if not isEmpty():
        return 0
    else:
        return 1

T = int(input())
for tc in range(T):
    data = str(input())
    # print(data)
    # print(make_gwalho(data))

    print(f"#{tc+1} {check_gwalho(make_gwalho(data))}")