# 분할정복

import sys
sys.stdin = open("토너먼트 카드게임.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    print(data)