# 상태공간트리를 구축하여 문제를 해결
# {1, 2, 3}의 powerset(부분집합)을 구하는 백트래킹 알고리즘

def process_solution(a, k):
    for i in range(1, k+1):
        if a[i]:
            print(data[i], end = " ")
    print()

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)    # 답이면 원하는 작업을 함
    else:
        k += 1
        ncandidates = make_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3]
a = [0] * NMAX        # powerset을 저장할 배열
backtrack(a, 0, 3)    # a, k, 3개의 원소를 가지는 powerset