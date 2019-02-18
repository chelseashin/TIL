# 계산기

# 2 + 3 * 4 / 5인 수식을 2345/*+ 가 되도록 출력

# 나의 풀이 - 피연산자와 연산자로만 분리
# str = "2+3*4/5"
#
# num = []
# cal = []
# for i in str:
#     if i.isdigit():
#         num.append(i)
#     else:
#         cal.append(i)
# print(''.join(num + cal))



# 연산자 stack에 pop한 값을 붙여줌
str = "2+3*4/5"
stack = []
for i in range(len(str)):
    if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
        stack.append(str[i])
    else:
        print(str[i], end = "")

while len(stack) != 0:
    print(stack.pop(), end= "")
