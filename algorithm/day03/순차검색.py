# 순차 검색 - while문
data = [4, 9, 11, 23, 2, 19, 7]
key = 19

def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i = i+1

    if i < n :
        return i
    else:
        return -1

print(sequentialSearch(data, len(data), key))



# 순차검색 - for문

data = [4, 9, 11, 23, 2, 19, 7]
key = 19

def sequentialSearch(a, n, key):
    for i in range(n):
        if data[i] == key:
            return i          # 있으면 위치 리턴
    return -1                 # 없으면 -1 리턴

print(sequentialSearch(data, len(data), key))