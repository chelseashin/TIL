import sys
sys.stdin = open("연습3.txt")

V, E = map(int, input().split())  # 정점의 개수: V, 간선의 개수 : E
data = list(map(int, input().split()))