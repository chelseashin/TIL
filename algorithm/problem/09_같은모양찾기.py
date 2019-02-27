import sys
sys.stdin = open("같은모양찾기.txt")

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

P = int(input())
pattern = [list(map(int, input())) for _ in range(P)]
