# Counting Sort(카운팅정렬)
# 시간복잡도 : O(n+k)
# n은 리스트의 개수, k는 정수의 최대값

def CountingSort(a, b, c):
    for i in range(len(a)):
        c[a[i]] += 1
    for i in range(1, len(c)):
        c[i] += c[i-1]
    for i in range(len(a)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1



a = [ 1, 4, 5, 1, 2, 4, 5, 7, 9, 3]
b = [0] * len(a)
c = [0] * 10
CountingSort(a, b, c)
print(b)