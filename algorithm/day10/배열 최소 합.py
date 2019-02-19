# 백트래킹 재귀 순열
import sys
sys.stdin = open("배열 최소 합.txt")


def process_solution(a, k):
    for i in range(1, k + 1):
        print(data[a[i]], end="")
    print()

def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)  # 답이면 원하는 작업을 한다.
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    Min = 0
    for i in range(len(N)):
        for j in range(len(N)):
            if arr[i][j] <= Min:
                Min = arr[i][j]
