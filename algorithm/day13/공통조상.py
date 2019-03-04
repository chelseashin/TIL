import sys
sys.stdin = open("공통조상.txt", "r")

T = int(input())
for tc in range(T):
    V, E, A, B = map(int, input().split())
    data = list(map(int, input().split()))
