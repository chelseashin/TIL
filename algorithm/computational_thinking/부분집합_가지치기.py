A = [0 for _ in range(N)]    # 원소의 포함여부 저장(0, 1)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n, sum):
    global count
    if sum == 10:
        count += 1
        print("%d : "% count, end="")    # 생성되는 부분 배열의 갯수 출력
        for i in range(n):
            if A[i] == 1:
                print("%d" % data[i], end="")
        print()

def powerset(n, k, sum):    # n : 원소의 갯수, k : 현재 depth
    global total
    if sum > 10: return
    total += 1
    if n == k:
        printSet(n, sum)
    else:
        A[k] = 1
