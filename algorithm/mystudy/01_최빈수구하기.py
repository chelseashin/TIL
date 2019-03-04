import sys
sys.stdin = open("최빈수구하기.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)

    D = {i : data.count(i) for i in set(data)}
    # 위와 같음
    # D = {}
    # for i in range(len(data)):
    #     D.update({i : data.count(i)})
    max_num = 0
    max_value = 0
    for num, value in D.items():
        if max_value < value:
            max_value = value
            max_num = num
    print("#{} {}".format(tc+1, max_num))

# 예시)
# N = 13
# data = [10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3]
# # print(len(set(data)))  # 8
# D = {i : data.count(i) for i in set(data)}
# print(D)
#
# max_num = 0
# max_value = 0
# for num, value in D.items():
#     if max_value < value:
#         max_value = value
#         max_num = num
# print(max_num)
