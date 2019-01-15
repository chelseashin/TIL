# 오름차순으로 풀기
# def bubbleSort(data):
#     for i in range(len(data)-1, 0, -1):   # 범위의 끝 위치 : 4, 3, 2, 1 순서로 들어옴
#         for j in range(0, i): # 4, 3, 2, 1 : 오름차순
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]




# 내림차순으로 풀기 - 부등호만 바꾸면 됨!
# def bubbleSort(data):
#     for i in range(len(data)-1, 0, -1):   # 범위의 끝 위치 : 4, 3, 2, 1 순서로 들어옴
#         for j in range(0, i): # 4, 3, 2, 1 : 오름차순
#             if data[j] < data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]


data = [55, 7, 78, 12, 42]      # 정렬할 리스트
# bubbleSort(data)
data.reverse()
print(data)