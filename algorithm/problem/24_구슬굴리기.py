import sys
sys.stdin = open("구슬굴리기.txt")

R, C = map(int, input().split())
arr = [list(map(int, input())) for _ in range(R)]
N = int(input())
dir = list(map(int, input().split()))   # 2 3 1 4 1 3
