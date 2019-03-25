# 부분집합 합 문제 구현하기
# 아래의 10개의 정수 집합에 대한 모든 부분 집합 중
# 원소의 합이 10이 되는 부분 집합을 모두 출력하시오

count = 0
N = 10
A = [0 for _ in range(N)]    # 원소의 포함여부 저장(0, 1)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n):
    global count
    print("%d : "%(count), end="")
    for i in range(n):
        if A[i] == 1:
            print("%d" % data[i], end="")
    print()

def powerset(n, k):
    global total
    total += 1
    if n == k:          # Basis Part
        printSet(n)
    else:
        A[k] = 1            # k번 요소 있으면
        powerset(n, k+1)    # 다음 요소 포함 여부 결정
        A[k] = 0            # k번 요소 없으면
        powerset(n, k+1)    # 다음 요소 포함 여부 결정

powerset(N, 0)
print("호출횟수 : {}".format(total))