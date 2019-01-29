def atoi(string):
    value = 0
    i = 0
    while i < len(string):
        c = string[i]
        if c >= '0' and c <= '9':
            digit = ord(c) - ord('0')    # ord()함수 : 아스키코드로 바꾸기
        else:
            break
        value = (value * 10) + digit;
        i += 1
    return value

a = "123"
print(type(a))
b = atoi(a)
print(type(b))
c = int(a)
print(type(c))

# str()함수를 사용하지 않고, itoa() 를 구현해봅시다.
#
# def itoa(x):
#     str = list()
#     y =  0
#     while True:
#         y = x % 10
#         str.append(chr(y + ord('0')))
#         x //= 10
#         if x == 0:
#             break
#             i += 1
#
#     str.reverse()
#     str = "".join(str)
#     return str
#
# x = 123;
# print(x, type(x))
# str1 = itoa(x)
# print(str1, type(str1))
# str2 = str(x)
# print(str2, type(str2))
