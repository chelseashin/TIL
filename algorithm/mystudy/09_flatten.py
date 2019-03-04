import sys
sys.stdin = open("flatten.txt", "r")

T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)