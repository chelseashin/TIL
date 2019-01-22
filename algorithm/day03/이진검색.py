# 이진검색
# 제약조건 : 데이터에 정렬이 되어 있어야 함!!!!

def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if key == a[middle]:  # 검색 성공
            return middle
        elif key <= a[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1    # 검색 실패


key = 22
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(data, key))




