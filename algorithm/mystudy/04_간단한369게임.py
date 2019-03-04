# 나의 풀이
N = 100
# N = int(input())
check = ['3', '6', '9']
print_num = ""
result = []
for i in range(1, N+1):
    number = str(i)
    for num in number:
        if num in check:
            print_num += "-"
    if len(print_num) == len(number):
        result.append(print_num)
    elif len(print_num):
        result.append(print_num)
    else:
        result.append(number)
    print_num = ""   # 초기화
print(" ".join(result))


# 다른 풀이
# cnt = 1
# clap = ['3', '6', '9']
#
# while cnt < N+1:
#     save = 0
#     temp = list(str(cnt))
#     for i in range(len(temp)):
#         if temp[i] in clap:
#             save += 1
#     if save > 0:
#         print("-"*save, end="")
#     else:
#         for i in range(len(temp)):
#             print(f"{temp[i]}", end="")
#
#     print(" ", end="")
#     cnt += 1

# 다른 풀이 2
# num =int(input())
# count =0
# for j in range(1, num +1):
#     n = j
#     count =0
#     while(int(n) !=0):
#         mod =int(n % 10)
#         if((mod % 3 ==0) and (mod !=0)):
#             count +=1
#         n /=int(10)
#     if(count ==0):
#         print(j, end =" ")
#     else:
#         while(count !=0):
#             print("-", end ="")
#             count -=1
#         print(" ", end ="")