import sys
sys.stdin = open("구간합.txt", "r")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # print(data)