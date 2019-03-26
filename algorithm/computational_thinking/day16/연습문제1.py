# 0과 1로 이루어진 1차원 배열에서 7개 byte를 묶어서 10진수로 출력하기
# 0, 120, 12, 7, 76, 24, 60, 121, 124, 103

# arr = [0,0,0,0,0,0,0,1,1,1,     1,0,0,0,0,0,0,1,1,0,    0,0,0,0,0,1,1,1,1,0,
#        0,1,1,0,0,0,0,1,1,0,     0,0,0,1,1,1,1,0,0,1,    1,1,1,0,0,1,1,1,1,1,
#        1,0,0,1,1,0,0,1,1,1]
#
# for i in range(10):
#     n = 0
#     for j in range(i*7, i*7+7, 1):
#         n = n*2+arr[j]
#     print(n, end=" ")
# print()

# 비트연산 예제1
# def Bbit_print(i):
#     output = ""
#     for j in range(7, -1, -1):
#         output += "1" if i&(1<<j) else "0"
#         print(output)
#
# for i in range(-5, 6):
#     print("%3d" = "%" end=" ")
#     Bbit_print()

# 비트연산예제5
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1"
        if i and (1 << j):
            print(output)
        else:
            print("0")

a = 0x86
key = 0xAA
